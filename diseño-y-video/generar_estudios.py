#!/usr/bin/env python3
"""Generate a still-image video with Ken Burns zoom using approaches that work."""
import subprocess, os

cd = "/home/node/workspace/videos-con-movimiento"
os.chdir(cd)
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
IMG = "estudiantes_grupo.jpg"  # 113KB, students group
OUT = "final_estudios_v2.mp4"

if not os.path.exists(IMG):
    print(f"❌ {IMG} not found")
    exit(1)

size = os.path.getsize(IMG)
print(f"Image: {IMG} ({size} bytes)")

# Strategy: generate frames with ImageMagick-like approach using ffmpeg
# First let's try without zoompan - just static image
vf = f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
vf += f",drawtext=fontfile={SANS}:text='ESTUDIA EN ESPANA':fontcolor=white:fontsize=44:bordercolor=black:borderw=4:x=(w-text_w)/2:y=60"

cmd = [
    "ffmpeg",
    "-i", IMG,
    "-vf", vf,
    "-t", "7",
    "-y", OUT
]
print("Generating without zoompan...")
r = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(OUT) and os.path.getsize(OUT) > 100000:
    print(f"✅ {OUT}: {os.path.getsize(OUT)} bytes")
else:
    print(f"❌ Failed: {r.stderr[-200:]}")

