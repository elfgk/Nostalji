import cv2 as cv
import numpy as np
import gradio as gr

# Siyah beyaz filtre uygulayan fonksiyon
def nostalji(image):
    img = np.array(image)  # Gradio'dan gelen resim PIL formatında, numpy'a çeviriyoruz
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray_image

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("# Görseli Siyah Beyaza Çevir")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin")

    # Görsel giriş ve çıkış bileşenleri
    image_input = gr.Image(type="pil", label="Giriş Resmi")
    image_output = gr.Image(type="numpy", label="Sonuç Resmi")

    image_input.change(nostalji, inputs=image_input, outputs=image_output)

# Gradio arayüzünü başlat
if __name__ == "__main__":
    demo.launch(share=True)
