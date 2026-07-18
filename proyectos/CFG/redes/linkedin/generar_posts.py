#!/usr/bin/env python3
"""Genera posts profesionales para LinkedIn de CFG-Seguros."""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
import os
import requests
from io import BytesIO

# Imágenes profesionales para LinkedIn
IMAGES = {
    1: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800",
    2: "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800",
    3: "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800",
}

POSTS = {
    1: {
        "title": "Nace CFG-Seguros en LinkedIn",
        "body": "Hoy damos un paso más para estar donde\nnuestros clientes nos necesitan.\n\nComo Colaborador de Grupo Galilea, ofrecemos:\n\n🏠 Hogar · 🚗 Coche · ❤️ Salud\n👴 Vida · 💼 Empresas · 💰 Planes de Ahorro\n\nAsesoramiento personalizado, sin compromiso.",
        "cta": "info@cfg-seguros.com"
    },
    2: {
        "title": "¿Sabías que el 60% de conductores\npodría ahorrar en su seguro?",
        "body": "Cada año millones renuevan sin comparar.\nTe ayudamos a:\n\n✅ Comparar entre aseguradoras\n✅ Ajustar coberturas a tu medida\n✅ Evitar pagar por lo que no usas\n✅ Conseguir asistencia 24h\n\nEstudio gratuito en 24h.",
        "cta": "info@cfg-seguros.com"
    },
    3: {
        "title": "Corredor vs Agente: ¿Cuál es la diferencia?",
        "body": "Agente → Trabaja para UNA aseguradora\nCorredor → Trabaja para TI\n\nEn CFG-Seguros somos corredores.\nBuscamos la mejor opción entre todas\nlas aseguradoras del mercado.\n\nTu interés es lo primero.",
        "cta": "info@cfg-seguros.com"
    }
}

def download_image(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def make_post(num, data, bg_img):
    W, H = 1080, 1080  # Cuadrado para LinkedIn
    
    bg = bg_img.copy().resize((W, H), Image.LANCZOS)
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.3)
    
    overlay = Image.new("RGB", (W, H), (5, 15, 35))
    img = Image.blend(bg, overlay, 0.25)
    draw = ImageDraw.Draw(img)
    
    base = "/usr/share/fonts/truetype/noto/"
    font_title = ImageFont.truetype(base + "NotoSans-Bold.ttf", 52)
    font_body  = ImageFont.truetype(base + "NotoSans-Regular.ttf", 32)
    font_cta   = ImageFont.truetype(base + "NotoSans-Bold.ttf", 36)
    font_meta  = ImageFont.truetype(base + "NotoSans-Regular.ttf", 22)
    
    white = (255, 255, 255)
    accent = (0, 185, 235)
    
    # Barra superior
    draw.rectangle([0, 0, W, 60], fill=(0, 0, 0, 200))
    draw.text((40, 16), "CFG-SEGUROS", font=font_meta, fill=accent)
    draw.text((W-280, 16), "Colaborador Grupo Galilea", font=font_meta, fill=(170, 170, 170))
    
    # Línea accent
    draw.rectangle([0, 350, W, 355], fill=accent)
    
    # Título
    title_lines = data['title'].split("\n")
    y = 400
    for line in title_lines:
        draw.text((60, y), line, font=font_title, fill=white)
        y += 60
    
    # Cuerpo
    body_lines = data['body'].split("\n")
    y = 580
    for line in body_lines:
        if y > H - 160:
            break
        if line.strip() == "":
            y += 10
        elif any(line.strip().startswith(x) for x in ("✅","🏠","🚗","❤️","👴","💼","💰")):
            draw.text((80, y), line, font=font_body, fill=accent)
        else:
            draw.text((80, y), line, font=font_body, fill=white)
        y += 42
    
    # CTA
    cta_y = H - 130
    cta_w = 480
    cta_x = (W - cta_w) // 2
    draw.rounded_rectangle([cta_x, cta_y, cta_x+cta_w, cta_y+60], radius=8, fill=accent)
    draw.text((W//2, cta_y+8), "📧  " + data['cta'], font=font_cta, fill=(0, 0, 0), anchor="mt")
    
    # Footer
    draw.line([(60, H-55), (W-60, H-55)], fill=(60, 70, 95), width=2)
    draw.text((60, H-40), "CFG-Seguros · Colaborador Grupo Galilea · cfg-seguros.com", font=font_meta, fill=(140, 140, 145))
    
    return img


outdir = "/home/node/workspace/proyectos/CFG/redes/linkedin/imagenes"
os.makedirs(outdir, exist_ok=True)

for num in sorted(IMAGES.keys()):
    print(f"Post {num}: descargando imagen...")
    bg = download_image(IMAGES[num])
    img = make_post(num, POSTS[num], bg)
    path = os.path.join(outdir, f"post_{num:02d}.png")
    img.save(path, quality=95)
    print(f"  ✅ {path}")

print("\n🎉 TODOS GENERADOS")
