#!/usr/bin/python3
"""Generate all 7 final videos with proper text overlays."""
import subprocess, os

os.chdir("/home/node/workspace/videos-con-movimiento")
FONTS = "/usr/share/fonts/truetype/dejavu"
SANS = f"{FONTS}/DejaVuSans-Bold.ttf"

videos = [
    ("dinero.mp4", "final_ahorro.mp4", "AHORRA CON INTELIGENCIA", "crecimientofinancieroglobal.com"),
    ("trading.mp4", "final_inversiones.mp4", "INVIERTE CON CONFIANZA", "crecimientofinancieroglobal.com"),
    ("negocios.mp4", "final_seguros.mp4", "PROTEGE A TU FAMILIA", "cfg-seguros.com"),
    ("salud.mp4", "final_salud.mp4", "CUIDA TU SALUD", "cfg-seguros.com"),
    ("viajes.mp4", "final_viajes.mp4", "VIAJA TRANQUILO", "crecimientofinancieroglobal.com"),
    ("exito.mp4", "final_estudios.mp4", "ESTUDIA EN ESPANA", "crecimientofinancieroglobal.com"),
]

for src, out, text, domain in videos:
    if not os.path.exists(src):
        print(f"❌ {src} not found")
        continue
    size = os.path.getsize(src)
    if size < 100000:
        print(f"❌ {src} too small ({size}b)")
        continue
    
    # Get video dimensions
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "default=noprint_wrappers=1", src],
        capture_output=True, text=True
    )
    lines = probe.stdout.strip().split("\n")
    w = int([l for l in lines if "width=" in l][0].split("=")[1])
    h = int([l for l in lines if "height=" in l][0].split("=")[1])
    
    print(f"🎬 {out}: {src} ({w}x{h}) -> '{text}'")
    
    # Determine if we need scale+pad or scale+crop
    target_ratio = 1280/720  # ~1.778 (9:16)
    source_ratio = h/w
    
    if source_ratio >= target_ratio:
        # Source is more vertical than target - crop sides
        vf = f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
    else:
        # Source is less vertical - pad top/bottom
        vf = f"scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2:color=black"
    
    vf += f",drawtext=fontfile={SANS}:text='{text}':fontcolor=white:fontsize=38:bordercolor=black:borderw=3:x=(w-text_w)/2:y=60"
    vf += f",drawtext=fontfile={SANS}:text='{domain}':fontcolor=yellow:fontsize=22:bordercolor=black:borderw=2:x=(w-text_w)/2:y=h-70"
    
    cmd = ["ffmpeg", "-i", src, "-t", "10", "-vf", vf, "-c:a", "copy", "-y", out]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out) and os.path.getsize(out) > 100000:
        print(f"  ✅ {os.path.getsize(out)/1048576:.1f} MB")
    else:
        print(f"  ❌ FAILED: {result.stderr[-200:]}")

# House video with Ken Burns
if os.path.exists("casa.jpg"):
    print(f"🎬 final_hogar.mp4: casa.jpg (zoom)")
    vf = f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
    vf += f",zoompan=z=1.015:d=250:m=0:s=720x1280"
    vf += f",drawtext=fontfile={SANS}:text='TU HOGAR PROTEGIDO':fontcolor=white:fontsize=38:bordercolor=black:borderw=3:x=(w-text_w)/2:y=60"
    vf += f",drawtext=fontfile={SANS}:text='cfg-seguros.com':fontcolor=yellow:fontsize=22:bordercolor=black:borderw=2:x=(w-text_w)/2:y=h-70"
    cmd = ["ffmpeg", "-loop", "1", "-i", "casa.jpg", "-t", "10", "-vf", vf, "-c:a", "copy", "-y", "final_hogar.mp4"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists("final_hogar.mp4") and os.path.getsize("final_hogar.mp4") > 100000:
        print(f"  ✅ {os.path.getsize('final_hogar.mp4')/1048576:.1f} MB")
    else:
        print(f"  ❌ FAILED")

print("\n=== FINAL LIST ===")
for f in sorted(os.listdir(".")):
    if f.startswith("final_") and f.endswith(".mp4"):
        sz = os.path.getsize(f)
        print(f"{'✅' if sz > 100000 else '❌'} {f}: {sz/1048576:.1f} MB")
