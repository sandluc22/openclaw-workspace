#!/usr/bin/env python3
"""Genera posts profesionales para Facebook de CFG Seguros."""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
import os
import requests
from io import BytesIO

# ─── Imágenes Unsplash (profesionales, personas reales) ───
IMAGES = {
    1: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800",   # Presentación - ejecutiva
    2: "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800",   # Hogar - casa
    3: "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800",      # Coche
    4: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800",   # Salud - persona activa
    5: "https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800",      # Empresas - oficina
    6: "https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=800",   # Vida - familia
    7: "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=800",      # Ahorro - inversión
}

POSTS = {
    1: {
        "emoji": "🛡️",
        "title": "Nace CFG Seguros",
        "subtitle": "Tu correduría de confianza",
        "body": "Llevamos años asesorando a particulares y empresas.\nHoy damos el salto a las redes para estar más cerca de ti.\n\nComo Colaborador de Grupo Galilea, trabajamos con las\nprincipales aseguradoras del mercado.\n\n🏠 Hogar · 🚗 Coche · ❤️ Salud\n👴 Vida · 💼 Empresas · 💰 Ahorro\n\nAsesoramiento personalizado, sin compromiso.",
        "cta": "info@cfg-seguros.com"
    },
    2: {
        "emoji": "🏠",
        "title": "Tu hogar, protegido",
        "subtitle": "¿Tu hogar está realmente protegido?",
        "body": "Un seguro de hogar cubre más de lo que imaginas.\n\n✅ Daños por agua\n✅ Rotura de cristales\n✅ Responsabilidad civil\n✅ Cerrajería 24h\n✅ Defensa jurídica\n\nInfórmate sin compromiso.",
        "cta": "info@cfg-seguros.com"
    },
    3: {
        "emoji": "🚗",
        "title": "Seguro de Coche",
        "subtitle": "¿Estás pagando de más?",
        "body": "Cada año miles de conductores renuevan sin comparar.\nTe ayudamos a encontrar una opción mejor.\n\n🟢 Terceros\n🟡 Terceros ampliado\n🔴 Todo riesgo\n\nAsistencia en carretera 24h incluida.",
        "cta": "info@cfg-seguros.com"
    },
    4: {
        "emoji": "❤️",
        "title": "Tu salud sin esperas",
        "subtitle": "Especialista en menos de 48h",
        "body": "Accede a los mejores cuadros médicos privados.\n\n✅ Consultas sin esperas\n✅ Pruebas diagnósticas en días\n✅ Urgencias 24h\n✅ Hospitalización individual\n\nTu salud no espera.",
        "cta": "info@cfg-seguros.com"
    },
    5: {
        "emoji": "💼",
        "title": "Autónomos y Empresas",
        "subtitle": "Protege tu negocio",
        "body": "Una reclamación, un accidente o una avería\npueden parar tu actividad.\n\n✅ Responsabilidad civil profesional\n✅ Accidentes laborales\n✅ Cobertura de locales\n✅ Cese de actividad\n\nEstudio personalizado para tu sector.",
        "cta": "info@cfg-seguros.com"
    },
    6: {
        "emoji": "👴",
        "title": "Seguro de Vida",
        "subtitle": "Protege a los tuyos",
        "body": "Si hay personas que dependen de ti, es responsabilidad.\n\n✔️ Fallecimiento por cualquier causa\n✔️ Invalidez permanente\n✔️ Enfermedades graves\n\nTranquilidad para tu familia.",
        "cta": "info@cfg-seguros.com"
    },
    7: {
        "emoji": "💰",
        "title": "Ahorro e Inversión",
        "subtitle": "¿Tu dinero trabaja para ti?",
        "body": "Con la inflación, tener el dinero parado es perder.\n\n📈 Plan de Ahorro\n📈 Planes de Pensiones\n📈 PIAS\n📈 Seguros de Ahorro\n\nPrimera consulta gratuita.",
        "cta": "info@cfg-seguros.com"
    }
}

def download_image(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def make_post(num, data, bg_img):
    W, H = 1080, 1350
    
    # Fondo
    bg = bg_img.copy().resize((W, H), Image.LANCZOS)
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.3)
    
    # Overlay oscuro
    overlay = Image.new("RGB", (W, H), (5, 15, 35))
    img = Image.blend(bg, overlay, 0.25)
    draw = ImageDraw.Draw(img)
    
    # Fuentes - NOTO SANS
    base = "/usr/share/fonts/truetype/noto/"
    font_title   = ImageFont.truetype(base + "NotoSans-Bold.ttf", 72)
    font_sub     = ImageFont.truetype(base + "NotoSans-Medium.ttf", 40)
    font_body    = ImageFont.truetype(base + "NotoSans-Regular.ttf", 36)
    font_cta     = ImageFont.truetype(base + "NotoSans-Bold.ttf", 42)
    font_meta    = ImageFont.truetype(base + "NotoSans-Regular.ttf", 26)
    
    white = (255, 255, 255)
    accent = (0, 185, 235)
    
    # ─── BARRA SUPERIOR ───
    draw.rectangle([0, 0, W, 80], fill=(0, 0, 0, 200))
    draw.text((50, 22), "CFG SEGUROS", font=font_meta, fill=accent)
    draw.text((W-350, 22), "Colaborador Grupo Galilea", font=font_meta, fill=(170, 170, 170))
    
    # ─── LÍNEA ACCENT ───
    ly = 420
    draw.rectangle([0, ly, W, ly+5], fill=accent)
    
    # ─── TÍTULO ───
    draw.text((60, 460), f"{data['emoji']}  {data['title']}", font=font_title, fill=white)
    
    # ─── SUBTÍTULO ───
    draw.text((60, 560), data['subtitle'], font=font_sub, fill=accent)
    
    # ─── CUERPO ───
    body_lines = data['body'].split("\n")
    y = 660
    for line in body_lines:
        if y > H - 200:
            break
        if line.strip() == "":
            y += 12
        elif any(line.strip().startswith(x) for x in ("✅","✔️","🟢","🟡","🔴","📈","🏠","🚗","❤️","👴","💰","💼")):
            draw.text((80, y), line, font=font_body, fill=accent)
        else:
            draw.text((80, y), line, font=font_body, fill=white)
        y += 48
    
    # ─── CTA ───
    cta_y = H - 150
    cta_w = 520
    cta_x = (W - cta_w) // 2
    draw.rounded_rectangle([cta_x, cta_y, cta_x+cta_w, cta_y+65], radius=8, fill=accent)
    draw.text((W//2, cta_y+10), "📧  " + data['cta'], font=font_cta, fill=(0, 0, 0), anchor="mt")
    
    # ─── FOOTER ───
    draw.line([(60, H-65), (W-60, H-65)], fill=(60, 70, 95), width=2)
    draw.text((60, H-48), "CFG Seguros · Colaborador Grupo Galilea · Asesoramiento personalizado", font=font_meta, fill=(140, 140, 145))
    
    return img


outdir = "/home/node/workspace/proyectos/CFG/redes/facebook/imagenes"
os.makedirs(outdir, exist_ok=True)

for num in sorted(IMAGES.keys()):
    print(f"Post {num}: descargando imagen...")
    bg = download_image(IMAGES[num])
    img = make_post(num, POSTS[num], bg)
    path = os.path.join(outdir, f"post_{num:02d}.png")
    img.save(path, quality=95)
    print(f"  ✅ {path}")

print("\n🎉 TODOS GENERADOS")
