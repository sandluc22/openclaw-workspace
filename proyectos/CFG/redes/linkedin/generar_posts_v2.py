#!/usr/bin/env python3
"""Regenera posts LinkedIn con correo MÁS GRANDE y visible."""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import requests
from io import BytesIO
import os

IMAGES = {
    1: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800",
    2: "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800",
    3: "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800",
}

POSTS = {
    1: {
        "title": "Nace CFG-Seguros en LinkedIn",
        "body": "Como Colaborador de Grupo Galilea, ofrecemos soluciones\npersonalizadas en seguros. Asesoramiento transparente,\nsin compromiso. Buscamos la mejor relación calidad-precio.",
        "cta": "info@cfg-seguros.com"
    },
    2: {
        "title": "¿Sabías que el 60% podría ahorrar?",
        "body": "Cada año millones renuevan sin comparar y las primas\nsuben. Te ayudamos a comparar entre aseguradoras,\najustar coberturas y evitar pagar por lo que no usas.\nEstudio comparativo gratuito en 24h.",
        "cta": "info@cfg-seguros.com"
    },
    3: {
        "title": "Corredor vs Agente",
        "body": "Agente → Trabaja para una aseguradora\nCorredor → Trabaja para TI\n\nEn CFG-Seguros somos corredores.\nBuscamos entre todas las aseguradoras\ndel mercado la mejor opción para ti.",
        "cta": "info@cfg-seguros.com"
    }
}

def download_image(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def make_post(num, data, bg_img):
    W, H = 1080, 1080
    bg = bg_img.copy().resize((W, H), Image.LANCZOS)
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.3)
    overlay = Image.new("RGB", (W, H), (5, 15, 35))
    img = Image.blend(bg, overlay, 0.25)
    draw = ImageDraw.Draw(img)
    
    base = "/usr/share/fonts/truetype/noto/"
    font_title = ImageFont.truetype(base + "NotoSans-Bold.ttf", 50)
    font_body  = ImageFont.truetype(base + "NotoSans-Regular.ttf", 32)
    font_cta   = ImageFont.truetype(base + "NotoSans-Bold.ttf", 40)
    font_meta  = ImageFont.truetype(base + "NotoSans-Regular.ttf", 22)
    
    white = (255, 255, 255)
    accent = (0, 185, 235)
    
    # Barra superior
    draw.rectangle([0, 0, W, 55], fill=(0, 0, 0, 200))
    draw.text((40, 14), "CFG-SEGUROS", font=font_meta, fill=accent)
    draw.text((W-280, 14), "Colaborador Grupo Galilea", font=font_meta, fill=(170, 170, 170))
    
    # Línea
    draw.rectangle([0, 340, W, 345], fill=accent)
    
    # Título
    y = 390
    for line in data['title'].split("\n"):
        draw.text((60, y), line, font=font_title, fill=white)
        y += 58
    
    # Cuerpo
    y = 520
    for line in data['body'].split("\n"):
        if y > 750:
            break
        if line.strip() == "":
            y += 10
        elif line.startswith("Agente") or line.startswith("Corredor") or line.startswith("En CFG"):
            draw.text((80, y), line, font=font_body, fill=accent)
        else:
            draw.text((80, y), line, font=font_body, fill=white)
        y += 42
    
    # CTA - MÁS GRANDE
    cta_y = H - 160
    cta_w = 600
    cta_h = 65
    cta_x = (W - cta_w) // 2
    draw.rounded_rectangle([cta_x, cta_y, cta_x+cta_w, cta_y+cta_h], radius=10, fill=accent)
    draw.text((W//2, cta_y + 14), "📧  " + data['cta'], font=font_cta, fill=(0, 0, 0), anchor="mt")
    
    # Footer
    draw.line([(60, H-55), (W-60, H-55)], fill=(60, 70, 95), width=2)
    draw.text((60, H-40), "CFG-Seguros · Colaborador Grupo Galilea · cfg-seguros.com", font=font_meta, fill=(140, 140, 145))
    
    return img


outdir = "/home/node/workspace/proyectos/CFG/redes/linkedin/imagenes"
os.makedirs(outdir, exist_ok=True)

for num in sorted(IMAGES.keys()):
    print(f"Post {num}: descargando...")
    bg = download_image(IMAGES[num])
    img = make_post(num, POSTS[num], bg)
    path = os.path.join(outdir, f"post_{num:02d}.png")
    img.save(path, quality=95)
    print(f"  ✅ {path}")

print("\n🎉 Todos generados con correo MÁS GRANDE")
