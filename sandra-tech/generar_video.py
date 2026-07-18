#!/usr/bin/env python3
"""Genera frames del vídeo review + lo combina con audio usando ffmpeg."""

from PIL import Image, ImageDraw, ImageFont
import subprocess, os, sys

W, H = 1080, 1920
FPS = 6
BG = (10, 10, 11)
ORANGE = (245, 158, 11)
WHITE = (228, 228, 231)
GRAY = (161, 161, 170)
DARK = (24, 24, 27)
DARK2 = (39, 39, 42)
GREEN = (34, 197, 94)
RED = (239, 68, 68)

OUTDIR = "/home/node/workspace/sandra-tech/frames"
os.makedirs(OUTDIR, exist_ok=True)

# Audio timing (seconds)
SEGMENTS = [
    ("intro", 0, 22),
    ("tamano", 22, 38),
    ("puertos", 38, 55),
    ("gan", 55, 72),
    ("prueba", 72, 92),
    ("proscontras", 92, 115),
    ("veredicto", 115, 140),
    ("outro", 140, 158),
]

# Load product image
product_img = None
try:
    product_img = Image.open("/home/node/workspace/sandra-tech/images/product1.jpg").resize((600, 600), Image.LANCZOS)
except:
    pass

def draw_text_centered(draw, text, y, font_size, color=WHITE, max_width=900):
    """Draw centered text with fallback for font."""
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Use textbbox for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, font=font, fill=color)

def draw_text_left(draw, text, x, y, font_size, color=WHITE):
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    draw.text((x, y), text, font=font, fill=color)

def make_frame(seg_name, frame_idx, total_frames_in_seg):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    

    
    t = frame_idx / FPS  # time within segment
    
    if seg_name == "intro":
        # Channel badge
        draw.rectangle([60, 60, 280, 110], fill=DARK, outline=DARK2)
        draw_text_left(draw, "SandraTech", 75, 72, 28, (161,161,170))
        
        # Product image
        if product_img:
            px = (W - 600) // 2
            img.paste(product_img, (px, 280))
        else:
            draw.rounded_rectangle([240, 280, 840, 880], radius=40, fill=DARK, outline=DARK2)
            draw_text_centered(draw, "⚡", 420, 200)
        
        # Title
        draw_text_centered(draw, "⚡ CARGADOR GaN 65W", 1000, 80, ORANGE)
        draw_text_centered(draw, "Review sincera", 1090, 50, WHITE)
        draw_text_centered(draw, "Sin postureo", 1150, 36, GRAY)
        
        # Subscribe
        draw.rounded_rectangle([380, 1300, 700, 1370], radius=20, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "🔔 Suscríbete", 1315, 28, GRAY)
        
    elif seg_name == "tamano":
        draw_text_centered(draw, "📏 El tamaño importa", 200, 70, WHITE)
        
        # Big charger box
        draw.rounded_rectangle([140, 400, 480, 750], radius=30, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "🔋", 480, 100)
        draw_text_centered(draw, "Tradicional", 620, 30, GRAY)
        draw_text_centered(draw, "grande y pesado", 660, 22, (82,82,91))
        
        # VS
        draw_text_centered(draw, "VS", 900, 60, ORANGE)
        
        # GaN charger box
        draw.rounded_rectangle([600, 420, 940, 700], radius=30, fill=DARK, outline=ORANGE)
        draw_text_centered(draw, "⚡", 490, 90)
        draw_text_centered(draw, "GaN 65W", 640, 28, ORANGE)
        draw_text_centered(draw, "50% más pequeño", 680, 22, GREEN)
        
        # Badge
        draw.rounded_rectangle([320, 950, 760, 1030], radius=25, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "👖 Cabe en cualquier sitio", 980, 32, GRAY)
        
        # Legend
        draw_text_centered(draw, "En el bolsillo · En la mochila · De viaje", 1100, 30, GRAY)
        
    elif seg_name == "puertos":
        draw_text_centered(draw, "🔌 3 puertos · Carga simultánea", 160, 65, WHITE)
        
        # Ports display
        devices = [("💻", "Portátil", 45), ("📱", "Móvil", 20), ("🎧", "Auriculares", 22)]
        for i, (emoji, label, watts) in enumerate(devices):
            x = 140 + i * 280
            # Box
            rx, ry = x, 320
            draw.rounded_rectangle([rx, ry, rx+240, ry+280], radius=24, fill=DARK, outline=DARK2)
            draw_text_centered(draw, emoji, ry+60, 70)
            draw_text_centered(draw, label, ry+150, 22, GRAY)
            draw_text_centered(draw, f"{watts}W", ry+190, 28, GREEN)
        
        # Total power
        draw.rounded_rectangle([340, 700, 740, 790], radius=30, fill=ORANGE)
        draw_text_centered(draw, "⚡ TOTAL: 65W", 730, 50, (10,10,11))
        
        # Cable note
        draw_text_centered(draw, "⚠️ Cable NO incluido", 900, 30, (239,68,68))
        
    elif seg_name == "gan":
        draw_text_centered(draw, "🧠 Tecnología GaN", 200, 70, WHITE)
        draw_text_centered(draw, "Nitruro de galio", 400, 45, GRAY)
        
        # GaN advantages grid
        advantages = [("🚀", "Más rápido", GREEN), ("❄️", "Menos calor", GREEN), 
                      ("📏", "50% menor", GREEN), ("🔒", "Seguro", GREEN)]
        for i, (emoji, label, color) in enumerate(advantages):
            col = i % 2
            row = i // 2
            x = 140 + col * 420
            y = 550 + row * 250
            draw.rounded_rectangle([x, y, x+360, y+200], radius=24, fill=DARK, outline=DARK2)
            draw_text_centered(draw, emoji, y+40, 60)
            draw_text_centered(draw, label, y+120, 32, color)
        
        # Compare text
        draw_text_centered(draw, "Carga rápida · Sin calentarse · Ocupa la mitad", 1400, 32, GRAY)
        
    elif seg_name == "prueba":
        draw_text_centered(draw, "⏱️ Prueba real de carga", 180, 65, WHITE)
        
        # Bars
        bars = [
            ("MacBook Air", "15% → 52% en 30 min", 52),
            ("Móvil", "20% → 80% en 45 min", 80),
            ("Auriculares", "10% → 100% en 30 min", 100),
        ]
        
        for i, (device, label, pct) in enumerate(bars):
            y = 380 + i * 200
            draw_text_left(draw, device, 140, y, 32, WHITE)
            draw_text_left(draw, label, 140, y+45, 26, GRAY)
            # Track
            track_y = y + 90
            draw.rounded_rectangle([140, track_y, 940, track_y+30], radius=15, fill=DARK2)
            # Fill
            fill_w = int((940 - 140) * pct / 100)
            draw.rounded_rectangle([140, track_y, 140+fill_w, track_y+30], radius=15, fill=ORANGE)
        
        # Summary
        draw.rounded_rectangle([240, 1200, 840, 1320], radius=25, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "⚡ Tres dispositivos a la vez", 1245, 32, GREEN)
        draw_text_centered(draw, "Sin perder rendimiento", 1290, 26, GRAY)
        
    elif seg_name == "proscontras":
        draw_text_centered(draw, "✅ Lo bueno  ·  ❌ Lo malo", 160, 60, WHITE)
        
        # Pros
        pros_x, pros_y = 100, 320
        draw.rounded_rectangle([pros_x, pros_y, pros_x+420, pros_y+520], radius=24, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "✅ Bueno", pros_y+30, 36, GREEN)
        
        pros_items = ["Carga 3 a la vez", "Tamaño compacto", "GaN eficiente", "No se calienta", "Solo 20€"]
        for i, item in enumerate(pros_items):
            draw_text_left(draw, item, pros_x+30, pros_y+80+i*80, 26, WHITE)
        
        # Cons
        cons_x, cons_y = 560, 320
        draw.rounded_rectangle([cons_x, cons_y, cons_x+420, cons_y+520], radius=24, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "❌ Malo", cons_y+30, 36, RED)
        
        cons_items = ["Cable no incluido", "Diseño sencillo", "USB-A 22W solo", "Sin clavija viajera"]
        for i, item in enumerate(cons_items):
            draw_text_left(draw, item, cons_x+30, cons_y+80+i*80, 26, WHITE)
        
    elif seg_name == "veredicto":
        # Big verdict box
        vx, vy = 140, 400
        draw.rounded_rectangle([vx, vy, W-vx, vy+500], radius=40, fill=ORANGE)
        draw_text_centered(draw, "🏆 VEREDICTO", vy+50, 50, (10,10,11))
        draw_text_centered(draw, "9 / 10", vy+150, 120, (10,10,11))
        draw_text_centered(draw, "Relación calidad-precio", vy+290, 36, (10,10,11))
        draw_text_centered(draw, "imbatible", vy+330, 36, (10,10,11))
        
        # Price box
        draw.rounded_rectangle([340, 1050, 740, 1200], radius=30, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "Precio", 1090, 28, GRAY)
        draw_text_centered(draw, "~19€", 1140, 70, ORANGE)
        
        # Use cases
        draw_text_centered(draw, "Ideal para:", 1350, 30, GRAY)
        draw_text_centered(draw, "✈️ Viajar  ·  💼 Teletrabajo  ·  🏠 Casa", 1400, 28, WHITE)
        
    elif seg_name == "outro":
        # Channel
        draw_text_centered(draw, "📺 SandraTech", 200, 50, ORANGE)
        draw_text_centered(draw, "Gracias por ver la review", 400, 50, WHITE)
        
        # CTA
        cx, cy = 190, 600
        draw.rounded_rectangle([cx, cy, W-cx, cy+180], radius=40, fill=ORANGE)
        draw_text_centered(draw, "🛒 Cómpralo aquí", cy+50, 55, (10,10,11))
        draw_text_centered(draw, "Enlace en descripción", cy+110, 28, (10,10,11,200))
        
        # Arrow
        draw_text_centered(draw, "👇", 900, 60)
        draw_text_centered(draw, "Enlace en la descripción", 980, 30, ORANGE)
        
        # Buttons
        draw.rounded_rectangle([340, 1100, 740, 1170], radius=20, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "🔔 Suscríbete", 1132, 26, GRAY)
        
        draw.rounded_rectangle([340, 1200, 740, 1270], radius=20, fill=DARK, outline=DARK2)
        draw_text_centered(draw, "📌 Guarda el vídeo", 1232, 26, GRAY)
    
    return img

def generate_all_frames():
    total_frames = 0
    for seg_name, start_sec, end_sec in SEGMENTS:
        duration = end_sec - start_sec
        n_frames = int(duration * FPS)
        for i in range(n_frames):
            img = make_frame(seg_name, i, n_frames)
            fname = f"frame_{total_frames:06d}.png"
            img.save(os.path.join(OUTDIR, fname))
            total_frames += 1
            if total_frames % 30 == 0:
                print(f"  Generated {total_frames} frames...")
    print(f"Total frames: {total_frames}")
    return total_frames

print("Generating frames...")
total = generate_all_frames()
print(f"\nDone! {total} frames generated in {OUTDIR}")
