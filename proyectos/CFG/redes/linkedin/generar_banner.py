#!/usr/bin/env python3
"""Genera banner para LinkedIn (1128x191 px) - CFG-Seguros"""

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

W, H = 1128, 191

# Imagen de fondo corporativa
url = "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=1200"
r = requests.get(url, timeout=10)
bg = Image.open(BytesIO(r.content)).convert("RGB").resize((W, H), Image.LANCZOS)

# Overlay oscuro
overlay = Image.new("RGB", (W, H), (5, 10, 30))
img = Image.blend(bg, overlay, 0.35)
draw = ImageDraw.Draw(img)

base = "/usr/share/fonts/truetype/noto/"
font_title = ImageFont.truetype(base + "NotoSans-Bold.ttf", 40)
font_sub   = ImageFont.truetype(base + "NotoSans-Regular.ttf", 24)
font_items = ImageFont.truetype(base + "NotoSans-Regular.ttf", 20)
font_cta   = ImageFont.truetype(base + "NotoSans-Bold.ttf", 22)

white = (255, 255, 255)
accent = (0, 185, 235)
gray = (180, 185, 190)

# Barra superior sutil
draw.rectangle([0, 0, W, 4], fill=accent)

# Texto izquierda
draw.text((40, 25), "CFG-SEGUROS", font=font_title, fill=white)
draw.text((40, 68), "Colaborador de Grupo Galilea", font=font_sub, fill=accent)

# Servicios
servicios = "🏠 Hogar  🚗 Coche  ❤️ Salud  👴 Vida  💼 Empresas  💰 Ahorro"
draw.text((40, 100), servicios, font=font_items, fill=white)

# Línea decorativa
draw.line([(40, 140), (700, 140)], fill=(60, 70, 95), width=2)

# CTA derecha
cta_x = 730
draw.text((cta_x, 35), "📧", font=font_cta, fill=accent)
draw.text((cta_x + 35, 35), "info@cfg-seguros.com", font=font_cta, fill=white)
draw.text((cta_x, 72), "🌐 cfg-seguros.com", font=font_cta, fill=accent)

# Botón "Seguir" simulado
btn_x = cta_x + 120
btn_y = 100
draw.rounded_rectangle([btn_x, btn_y, btn_x+130, btn_y+40], radius=6, fill=accent)
draw.text((btn_x+65, btn_y+7), "Asesoría gratuita", font=font_cta, fill=(0,0,0), anchor="mt")

outdir = "/home/node/workspace/proyectos/CFG/redes/linkedin"
img.save(f"{outdir}/banner_linkedin.png", quality=95)
print(f"✅ Banner LinkedIn: {outdir}/banner_linkedin.png")
