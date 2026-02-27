# ======================
# --- 0. LIBRERIAS ---
# ======================
import gradio as gr
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# ========================
# --- 1. CONFIGURACIÓN ---
# ========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
imsize = 256 # MODIFICAR TAMAÑO DE IMAGEN (384,192,256) SI USAS VERSIONES DE SPACE GRATUITAS PARA NO IR LENTO :P


# Transformación de entrada 

loader = transforms.Compose([
    transforms.Resize((imsize, imsize)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Transformación inversa (Desnormalizar para mostrar la imagen final)

unloader = transforms.Compose([
    transforms.Normalize(mean=[-0.485/0.229, -0.456/0.224, -0.406/0.225], 
                         std=[1/0.229, 1/0.224, 1/0.225]),
    transforms.Lambda(lambda x: x.clamp(0, 1)),
    transforms.ToPILImage()
])

# ===============================
# --- 2. FUNCIONES DE PÉRDIDA ---
# ===============================
def calc_content_loss(gen_features, content_features):
    return torch.mean((gen_features - content_features) ** 2)

def gram_matrix(tensor):
    _, c, h, w = tensor.size()
    tensor = tensor.view(c, h * w)
    return torch.mm(tensor, tensor.t()) / (c * h * w)

def calc_style_loss(gen_features, style_features):
    G_gen = gram_matrix(gen_features)
    G_style = gram_matrix(style_features)
    return torch.mean((G_gen - G_style) ** 2)

def calc_tv_loss(img):
    tv_h = torch.sum((img[:, :, 1:, :] - img[:, :, :-1, :]) ** 2)
    tv_w = torch.sum((img[:, :, :, 1:] - img[:, :, :, :-1]) ** 2)
    return tv_h + tv_w

# ============================
# --- 3. MODELO EXTRACTOR ---
# ============================
class VGGFeatureExtractor(nn.Module):
    def __init__(self):
        super().__init__()
        vgg = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1).features
        for param in vgg.parameters():
            param.requires_grad = False
        self.model = vgg.to(device).eval()
        self.style_layers = {'0': 'block1_conv1', '5': 'block2_conv1', '10': 'block3_conv1', '19': 'block4_conv1', '28': 'block5_conv1'}
        self.content_layers = {'30': 'block5_conv2'} 

    def forward(self, x):
        style_features = {}
        content_features = {}
        for name, layer in self.model._modules.items():
            x = layer(x)
            if name in self.style_layers: style_features[self.style_layers[name]] = x
            if name in self.content_layers: content_features[self.content_layers[name]] = x
        return content_features, style_features
        
# ========================================
# --- 4. FUNCIÓN PRINCIPAL PARA GRADIO ---
# ========================================
def run_style_transfer(content_img, style_img, content_weight, style_weight, tv_weight, iterations):
    if content_img is None or style_img is None:
        return None
    
    # Aplicamos las transformaciones (incluyendo el resize a 384x384)
    content_tensor = loader(content_img).unsqueeze(0).to(device, torch.float)
    style_tensor = loader(style_img).unsqueeze(0).to(device, torch.float)
    
    gen_img = content_tensor.clone().requires_grad_(True)
    extractor = VGGFeatureExtractor().to(device)
    
    target_content_features, _ = extractor(content_tensor)
    _, target_style_features = extractor(style_tensor)
    
    optimizer = optim.LBFGS([gen_img], max_iter=20)
    
    for i in range(int(iterations)):
        def closure():
            optimizer.zero_grad()
            gen_img.data.clamp_(-2.1, 2.6)
            
            gen_content_features, gen_style_features = extractor(gen_img)
            
            c_loss = calc_content_loss(gen_content_features['block5_conv2'], target_content_features['block5_conv2'])
            
            s_loss = 0
            for layer_name in target_style_features:
                s_loss += calc_style_loss(gen_style_features[layer_name], target_style_features[layer_name])
            s_loss /= len(target_style_features)
            
            t_loss = calc_tv_loss(gen_img)
            
            total_loss = (content_weight * c_loss) + (style_weight * s_loss) + (tv_weight * t_loss)
            total_loss.backward()
            return total_loss
            
        optimizer.step(closure)
        
    gen_img.data.clamp_(-2.1, 2.6)
    
    final_image = unloader(gen_img.cpu().squeeze(0))
    return final_image

# =======================================
# --- 5. INTERFAZ DE USUARIO (GRADIO) ---
# =======================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    
    # ENCABEZADO Y ENLACES
    gr.Markdown(
        """
        <div style="text-align: center;">
            <h1>🎨 Transferencia de Estilo Neuronal</h1>
            <p>Sube una imagen base y una imagen de estilo para combinarlas. <i>Nota: Las imágenes se redimensionan automáticamente para procesamiento rápido.</i></p>
            <p>
                <a href="https://github.com/MGranados64" target="_blank" style="text-decoration: none;">🐙 <b>Mi GitHub</b></a> &nbsp; | &nbsp; 
                <a href="https://huggingface.co/MGC1991MF" target="_blank" style="text-decoration: none;">🤗 <b>Mi perfil en Hugging Face</b></a>
            </p>
        </div>
        """
    )
    
    with gr.Row():
        with gr.Column():
            content_in = gr.Image(type="pil", label="Imagen Base (A)")
            style_in = gr.Image(type="pil", label="Imagen de Estilo (B)")
        with gr.Column():
            output_image = gr.Image(type="pil", label="Imagen Resultante (C)")
            
    with gr.Row():
        with gr.Column():
            gr.Markdown("### ⚙️ Ajustes del Modelo")
            c_weight = gr.Slider(minimum=0.1, maximum=10.0, value=1.0, step=0.1, label="Peso del Contenido (Estructura)")
            s_weight = gr.Slider(minimum=1000, maximum=1000000, value=100000, step=1000, label="Peso del Estilo (Arte)")
            tv_weight = gr.Slider(minimum=0, maximum=0.001, value=0.000001, step=0.000001, label="Suavizado (Variación Total)")
            iters = gr.Slider(minimum=2, maximum=20, value=5, step=1, label="Iteraciones")
            
            run_btn = gr.Button("¡Mezclar Imágenes!", variant="primary")

    run_btn.click(
        fn=run_style_transfer,
        inputs=[content_in, style_in, c_weight, s_weight, tv_weight, iters],
        outputs=output_image
    )

if __name__ == "__main__":
    demo.launch()