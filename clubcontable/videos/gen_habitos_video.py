import subprocess, os, sys

W=1280
H=720
FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

VIDEO_NUM = sys.argv[1]  # 3, 4, or 5
AUDIO_FILE = f"habitos{VIDEO_NUM}_audio_ext.mp3"
OUTPUT = f"habitos_video_0{VIDEO_NUM}_ok.mp4"

# Duración del audio
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
    '-of','default=noprint_wrappers=1:nokey=1',AUDIO_FILE]).strip())
IMG_TIME = dur / 18.0
print(f"DUR={dur}s, IMG_TIME={IMG_TIME}s")

# Textos para cada frame
if VIDEO_NUM == "3":
    tx = [
        "REGLA DE ORO\nDEL CAMBIO\nVideo 3",
        "No puedes extinguir\nun mal hábito.\nSolo puedes\nCAMBIARLO.",
        "Mantén la SEÑAL.\nMantén la\nRECOMPENSA.\nCambia la RUTINA.",
        "Ejemplo:\nTarea compleja\n→ café.\nRecompensa = pausa.",
        "Cambia la rutina:\nCaminar 5 min\nen lugar de café.\nMisma recompensa.",
        "La recompensa real\nNO es la obvia.\nHaz el experimento\nde 15 min.",
        "Cambia la rutina.\nEspera 15 min.\n¿Sigues teniendo\nel impulso?",
        "Contador con móvil:\nEstímulo → leer\nartículo sector.\n¿Funcionó?",
        "Los hábitos son\nautopistas\nneuronales.\nCrear una nueva\nlleva tiempo.",
        "El MOMENTO DE\nELECCIÓN:\nEntre la señal\ny la rutina.",
        "Pausa de 5 seg:\nCuenta hasta 5\nantes de actuar.\nElige otra ruta.",
        "Correo estresante:\n→ anotar y seguir\nen lugar de\nangustiarse.",
        "LA CREENCIA:\nNecesitas creer\nque puedes\ncambiar.",
        "El grupo es clave:\nVer a otros como\ntú que lo lograron\nte da fe.",
        "Comunidad de\ncontadores:\nCompartir éxitos\ny apoyarse.",
        "Empieza con UN\nhábito clave.\nEl que desencadena\ntodo lo demás.",
        "Planificar el día:\nClaridad →\nEnfoque →\nProductividad.",
        "Suscríbete y activa\nla campanita.\nComparte con otro\ncontador. 🔥"
    ]
elif VIDEO_NUM == "4":
    tx = [
        "HÁBITOS EN\nORGANIZACIONES\nVideo 4",
        "Las empresas también\ntienen hábitos.\nEn equipos y\ncultura laboral.",
        "El hábito del\nequipo exitoso:\nComunicación\nabierta y segura.",
        "Caso Starbucks:\nEntrenan el hábito\nde servir café\ncon conexión.",
        "Caso Alcoa:\nUn solo hábito\n(seguridad)\ntransformó toda\nla empresa.",
        "Para despachos:\nEl hábito de\nrevisión semanal\ncon el equipo.",
        "Rutina de reunión:\n¿Qué funcionó?\n¿Qué mejorar?\n¿Qué celebrar?",
        "Los líderes crean\nhábitos de equipo:\nEl ejemplo es\nel hábito más\npoderoso.",
        "Si el jefe llega\ntarde, todos\nllegan tarde.\nEl hábito se\ncontagia.",
        "Rituales de equipo:\nCafé de los lunes.\nCelebrar logros.\nRevisar juntos.",
        "Crisis = oportunidad:\nEl estrés rompe\nhábitos viejos\ny crea nuevos.",
        "Contador líder:\nTu equipo imita\ntus hábitos.\nSé el ejemplo.",
        "Hábito de mejora:\nCada viernes,\n¿qué hicimos\nmejor esta semana?",
        "Cultura organizacl:\nNo es misión.\nSon los hábitos\ndiarios de todos.",
        "Empieza con un\nhábito de equipo:\nLa reunión matutina\nde 10 min.",
        "Hábito → Rutina\n→ Cultura.\nAsí se transforma\nun despacho.",
        "Suscríbete y activa\nla campanita.\nComparte con otro\ncontador. 🔥"
    ]
elif VIDEO_NUM == "5":
    tx = [
        "EL PODER DE\nLA CREENCIA\nVideo 5",
        "La creencia es lo\nque sostiene el\ncambio a largo\nplazo.",
        "Duhigg: Las personas\nque mantienen el\ncambio son las\nque CREEN.",
        "No en el cambio\nmismo. Sino en\nque PUEDEN\ncambiarlo todo.",
        "AA funciona por\nla creencia:\nVer a otros que\nlo lograron.",
        "El grupo refuerza:\nNo estás solo.\nOtros como tú\nlo consiguieron.",
        "Para contadores:\nUna comunidad de\ncolegas que se\napoyan mutuamente.",
        "La fe no es\nreligión.\nEs certeza de\nque es posible.",
        "Cuando fallas:\nNo es el fin.\nEs aprendizaje.\nEl hábito sigue.",
        "El bucle se\nrefuerza con\ncada acierto.\nY con cada\nintento.",
        "Hábito de creencia:\nEscribe cada día\nun logro pequeño.\nTe recordará que\npuedes.",
        "El éxito deja\npistas:\nMira a quien ya\nlo logró y\naprende.",
        "Celebra los\npequeños pasos:\nCada día cuenta.\nCada esfuerzo\nsuma.",
        "Creer + Grupo +\nHábito clave =\nTransformación\nreal.",
        "El viaje de los\nhábitos no\ntermina nunca.\nEres obra en\nproceso.",
        "Gracias por verme.\nEste es el final\nde la serie.\nPero empieza tu\ncambio.",
        "Deja tu comentario,\nlos leo todos.\nSuscríbete.\nComparte. 🔥"
    ]

DIR = f"h{VIDEO_NUM}ok"
os.makedirs(DIR, exist_ok=True)

print("Generando frames...")
for i, t in enumerate(tx):
    num = f"{i:02d}"
    t_esc = t.replace("'","\\'").replace(":","\\:").replace("{","\\{").replace("}","\\}")
    cmd = [
        'ffmpeg','-y','-f','lavfi','-i',f'color=c=#1a1a2e:s={W}x{H}:d=1',
        '-vf',f"drawtext=text='{t_esc}':fontfile={FONT}:fontsize=30:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=20:line_spacing=8",
        '-frames:v','1',f'{DIR}/f_{num}.png'
    ]
    r = subprocess.run(cmd, capture_output=True, timeout=15)
    if r.returncode != 0:
        print(f"  f_{num} ERROR")
print(f"Frames: {len(os.listdir(DIR))}")

print("Generando clips...")
for i in range(len(tx)):
    num = f"{i:02d}"
    cmd = [
        'ffmpeg','-y','-loop','1','-framerate','12',
        '-i',f'{DIR}/f_{num}.png',
        '-c:v','libx264','-t',str(IMG_TIME),'-pix_fmt','yuv420p',
        '-preset','ultrafast','-crf','35',
        '-vf',f'scale={W}:{H}',
        '-an',f'{DIR}/c_{num}.ts'
    ]
    r = subprocess.run(cmd, capture_output=True, timeout=60)
    if r.returncode != 0:
        print(f"  c_{num} FAILED")
        sys.exit(1)
    dur_c = subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
        '-of','default=noprint_wrappers=1:nokey=1',f'{DIR}/c_{num}.ts']).strip()
    print(f"  c_{num}: {dur_c}s")

print("Concatenando...")
with open(f'{DIR}/concat.txt','w') as f:
    for i in range(len(tx)):
        f.write(f"file 'c_{i:02d}.ts'\n")
r = subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',f'{DIR}/concat.txt',
    '-c','copy',f'{DIR}/vn.mp4'], capture_output=True, timeout=60)
if r.returncode != 0:
    print(f"Concat ERROR")
    sys.exit(1)

print("Uniendo audio...")
r = subprocess.run(['ffmpeg','-y','-i',f'{DIR}/vn.mp4','-i',AUDIO_FILE,
    '-c:v','copy','-c:a','aac','-b:a','128k',
    '-movflags','+faststart',OUTPUT], capture_output=True, timeout=120)
if r.returncode != 0:
    print(f"Merge ERROR")
    sys.exit(1)

os.chmod(OUTPUT, 0o644)
final = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
    '-of','default=noprint_wrappers=1:nokey=1',OUTPUT]).strip())
size = os.path.getsize(OUTPUT)
print(f"✅ {OUTPUT}")
print(f"⏱ {final}s (~{int(final/60)} min)")
print(f"📦 {size/1024/1024:.1f} MB")
