#!/usr/bin/env python3
"""Generate a stylized 'Estudia en España' image with a graduation/academic theme."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

os.chdir("/home/node/workspace/videos-con-movimiento")
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Create a 720x1280 image
img = Image.new("RGB", (720, 1280), (10, 30, 60))  # dark blue background
draw = ImageDraw.Draw(img)

# Draw abstract elements
import math

# Draw a graduation cap shape at top
def draw_grad_cap(draw, cx, cy, size):
    # Square board
    draw.polygon([
        (cx - size, cy - size//2),
        (cx + size, cy - size//2),
        (cx + size//2, cy + size//2),
        (cx - size//2, cy + size//2)
    ], fill=(200, 170, 50))  # gold
    
    # Tassel
    draw.line([(cx + size//2, cy + size//2), (cx + size + 10, cy + size)], fill=(200, 170, 50), width=3)
    
    # Head under
    draw.ellipse([cx - size//2, cy + size//3, cx + size//2, cy + size + 20], fill=(80, 100, 140))

# Draw multiple elements
draw_grad_cap(draw, 360, 120, 80)

# Draw a globe or map of Spain
# Spain shape simplified
def draw_spain(draw, cx, cy, s):
    points = [
        (cx, cy-s*0.8), (cx+s*0.5, cy-s*0.6), (cx+s*0.8, cy-s*0.3),
        (cx+s*0.9, cy), (cx+s*0.7, cy+s*0.4), (cx+s*0.3, cy+s*0.6),
        (cx-s*0.2, cy+s*0.5), (cx-s*0.6, cy+s*0.3), (cx-s*0.8, cy),
        (cx-s*0.7, cy-s*0.3), (cx-s*0.4, cy-s*0.7)
    ]
    draw.polygon(points, fill=(50, 120, 200), outline=(200, 170, 50), width=3)

draw_spain(draw, 360, 320, 100)

# Draw books/stack
for i in range(3):
    y = 480 + i * 30
    draw.rectangle([(260, y), (460, y+22)], fill=(150+i*20, 100, 50+i*10), outline=(200,170,50), width=2)
    # Book spine detail
    draw.line([(360, y), (360, y+22)], fill=(200,170,50), width=1)

# Draw a graduation scroll/diploma
draw.rectangle([(300, 580), (420, 620)], fill=(220, 195, 80), outline=(180, 150, 40), width=2)
draw.ellipse([(300, 570), (320, 590)], fill=(200, 170, 50))
# Ribbon
draw.line([(310, 580), (310, 620)], fill=(180, 50, 50), width=4)

# Draw stars/sparkles around
for i in range(15):
    x = 50 + (i * 45) % 650
    y = 680 + (i * 37) % 400
    r = 3 + (i % 3)
    draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=(200, 170, 50))

# Draw small silhouette figures (students)
for i in range(4):
    sx = 100 + i * 180
    sy = 1080
    # Body
    draw.ellipse([(sx-15, sy-50), (sx+15, sy-20)], fill=(100, 100, 140))  # head
    draw.rectangle([(sx-12, sy-20), (sx+12, sy)], fill=(100, 100, 140))  # body
    # Arms up (celebration)
    draw.line([(sx-12, sy-15), (sx-25, sy-30)], fill=(100, 100, 140), width=3)
    draw.line([(sx+12, sy-15), (sx+25, sy-25)], fill=(100, 100, 140), width=3)

# Draw confetti dots
for i in range(30):
    cx = 30 + (i * 23) % 680
    cy = 1080 - (i * 17) % 200
    colors = [(200,170,50), (50,120,200), (180,50,50), (50,180,80)]
    draw.ellipse([(cx-3, cy-3), (cx+3, cy+3)], fill=colors[i%4])

# Draw decorative lines
for i in range(8):
    y = 650 + i * 30
    draw.line([(150, y), (570, y)], fill=(200, 170, 50, 100), width=1)

# Text: ESTUDIA EN ESPAÑA
try:
    font_large = ImageFont.truetype(SANS, 48)
    font_small = ImageFont.truetype(SANS, 22)
except:
    font_large = ImageFont.load_default()
    font_small = font_large

# Main text with shadow
text = "ESTUDIA EN"
bbox = draw.textbbox((0, 0), text, font=font_large)
tw = bbox[2] - bbox[0]
draw.text(((720 - tw) // 2, 770), text, fill=(200, 170, 50), font=font_large)

text2 = "ESPANA"
bbox2 = draw.textbbox((0, 0), text2, font=font_large)
tw2 = bbox2[2] - bbox2[0]
draw.text(((720 - tw2) // 2, 830), text2, fill=(200, 170, 50), font=font_large)

# Subtitle
sub = "Desde Colombia es posible"
bbox3 = draw.textbbox((0, 0), sub, font=font_small)
tw3 = bbox3[2] - bbox3[0]
draw.text(((720 - tw3) // 2, 910), sub, fill=(200, 200, 220), font=font_small)

# Add a gradient overlay at bottom
for i in range(40):
    alpha = int(255 * (1 - i/40))
    y = 1200 + i * 2
    draw.line([(0, y), (720, y)], fill=(10+i*3, 30+i*2, 60+i, alpha))

# Save a preview
img.save("/tmp/estudiantes_art.jpg", "JPEG", quality=92)
print(f"Generated: {(os.path.getsize('/tmp/estudiantes_art.jpg'))/1024:.0f}KB")

# Copy to working dir
import shutil
shutil.copy("/tmp/estudiantes_art.jpg", "estudiantes_art.jpg")
print("Copied to working dir")
