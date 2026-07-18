#!/usr/bin/env python3
"""Prepara frames para videos TikTok CFG-Seguros (vertical 1080x1920)"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import requests
from io import BytesIO
import os

OUTDIR = "/home/node/workspace/proyectos/CFG/redes/tiktok"
os.makedirs(OUTDIR, exist_ok=True)

W, H = 1080, 1920

VIDEOS = [
    {
        "name": "tiktok_01_errores_coche",
        "bg": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=1080",
        "slides": [
            {"text": "3 ERRORES que cometes\ncon tu seguro de coche", "sub": "Y cómo ahorrar hasta 300€ al año", "big": True},
            {"text": "❌ Error 1", "sub": "Renovar automáticamente\nsin comparar precios", "big": False},
            {"text": "❌ Error 2", "sub": "Pagar por coberturas\nque no necesitas", "big": False},
            {"text": "❌ Error 3", "sub": "No revisar la letra pequeña\ncuando algo cambia", "big": False},
            {"text": "✅ Solución", "sub": "En CFG-Seguros te ayudamos\na encontrar la mejor opción\nsin compromiso", "big": False},
            {"text": "CFG-SEGUROS", "sub": "Colaborador Grupo Galilea\n📧 info@cfg-seguros.com\n🌐 cfg-seguros.com", "big": False},
        ]
    },
    {
        "name": "tiktok_02_hogar",
        "bg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1080",
        "slides": [
            {"text": "¿Tu seguro de hogar\nte cubre esto?", "sub": "Lo que NO sabías y deberías revisar", "big": True},
            {"text": "🔍 Dato importante", "sub": "Muchas pólizas NO cubren\ndaños por agua si no hay\nmantenimiento preventivo", "big": False},
            {"text": "🔍 ¿Y la responsabilidad civil?", "sub": "Si tu mascota rompe algo\ndel vecino... ¿estás cubierto?", "big": False},
            {"text": "🔍 Robo fuera de casa", "sub": "¿Sabías que tu seguro de hogar\ncubre robos fuera del domicilio?", "big": False},
            {"text": "✅ Nosotros te lo aclaramos", "sub": "En CFG-Seguros revisamos\ntu póliza y te explicamos todo", "big": False},
            {"text": "CFG-SEGUROS", "sub": "Colaborador Grupo Galilea\n📧 info@cfg-seguros.com\n🌐 cfg-seguros.com", "big": False},
        ]
    },
]

def download_bg(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def make_slide(bg, text, sub, big=False):
    img = bg.copy().resize((W, H), Image.LANCZOS)
    enh = ImageEnhance.Brightness(img)
    img = enh.enhance(0.35)
    ov = Image.new("RGB", (W, H), (5, 10, 30))
    img = Image.blend(img, ov, 0.15)
    draw = ImageDraw.Draw(img)
    
    base = "/usr/share/fonts/truetype/noto/"
    if big:
        ft = ImageFont.truetype(base + "NotoSans-Bold.ttf", 80)
        fs = ImageFont.truetype(base + "NotoSans-Regular.ttf", 38)
    else:
        ft = ImageFont.truetype(base + "NotoSans-Bold.ttf", 64)
        fs = ImageFont.truetype(base + "NotoSans-Regular.ttf", 36)
    
    white = (255, 255, 255)
    accent = (0, 185, 235)
    
    # Texto principal centrado
    lines = text.split("\n")
    th = sum(draw.multiline_textbbox((0, 0), l, font=ft)[3] - draw.multiline_textbbox((0, 0), l, font=ft)[1] + 10 for l in lines)
    y = (H - th) // 2 - 60
    for l in lines:
        bb = draw.multiline_textbbox((0, 0), l, font=ft)
        tx = (W - (bb[2] - bb[0])) // 2
        draw.text((tx, y), l, font=ft, fill=white)
        y += (bb[3] - bb[1]) + 10
    
    # Subtitulo
    slines = sub.split("\n")
    y += 40
    for l in slines:
        bb = draw.multiline_textbbox((0, 0), l, font=fs)
        tx = (W - (bb[2] - bb[0])) // 2
        draw.text((tx, y), l, font=fs, fill=accent)
        y += (bb[3] - bb[1]) + 8
    
    # Barra inferior
    draw.rectangle([0, H-80, W, H], fill=(0, 0, 0, 180))
    draw.text((40, H-60), "CFG-Seguros", font=fs, fill=accent)
    return img

for vid in VIDEOS:
    print(f"\n🎬 {vid['name']}: descargando fondo...")
    bg = download_bg(vid['bg'])
    frames_dir = os.path.join(OUTDIR, vid['name'])
    os.makedirs(frames_dir, exist_ok=True)
    for i, slide in enumerate(vid['slides']):
        img = make_slide(bg, slide['text'], slide['sub'], slide['big'])
        path = os.path.join(frames_dir, f"slide_{i:02d}.png")
        img.save(path, quality=95)
        print(f"  ✅ slide {i+1}/{len(vid['slides'])}")

print("\n🎉 FRAMES GENERADOS")
