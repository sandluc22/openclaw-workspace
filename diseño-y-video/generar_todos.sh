#!/bin/bash
# Generar todos los vídeos con movimiento
# Asignación tema -> video

cd /home/node/workspace/videos-con-movimiento

FONTS=/usr/share/fonts/truetype/dejavu
SANS="${FONTS}/DejaVuSans-Bold.ttf"

# Limpiar outputs anteriores
rm -f final_*.mp4

# Función para crear vídeo con texto
# Argumentos: input output texto_superior segundos_inicio duracion
crear_video() {
  local INPUT=$1
  local OUTPUT=$2
  local TEXTO=$3
  local DURACION=${4:-10}
  
  # Obtener resolución original
  local INFO=$(ffprobe -v error -show_entries stream=width,height -of default=noprint_wrappers=1 "$INPUT" 2>/dev/null)
  local W=$(echo "$INFO" | grep width | head -1 | cut -d= -f2)
  local H=$(echo "$INFO" | grep height | head -1 | cut -d= -f2)
  
  echo "🎬 $OUTPUT: ${W}x${H} -> texto: $TEXTO"
  
  # Si es más grande que 720x1280, escalar y recortar a 720x1280 (9:16 perfecto)
  # Si es 540x960, escalar a 720x1280
  # Si es más ancho que alto (horizontal), recortar
  
  if [ "$H" -gt "$W" ]; then
    # Ya es vertical - escalar a 720x1280 manteniendo aspecto y recortando si necesario
    if [ "$H" -eq "$W" ] || [ "$((H * 9))" -eq "$((W * 16))" ]; then
      # Ya es 9:16 o cuadrado
      local VFILTER="scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2"
    else
      # Escalar para cubrir 720x1280 y recortar
      local VFILTER="scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
    fi
  else
    # Horizontal - escalar a 720x1280 recortando
    local VFILTER="scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
  fi
  
  # Añadir overlay oscuro (60% opacidad) + textos
  ffmpeg -i "$INPUT" -t "$DURACION" \
    -filter_complex \
    "[0:v]${VFILTER}[base]; \
     [base]drawbox=x=0:y=0:w=720:h=1280:c=black@0.3:t=fill[b30]; \
     [b30]drawtext=fontfile=${SANS}:text='${TEXTO}':fontcolor=white:fontsize=40:bordercolor=black:borderw=3:x=(w-text_w)/2:y=60:enable='between(t,0,${DURACION})'[txt1]; \
     [txt1]drawtext=fontfile=${SANS}:text='crecimientofinancieroglobal.com':fontcolor=#f5a623:fontsize=24:bordercolor=black:borderw=2:x=(w-text_w)/2:y=h-80:enable='between(t,0,${DURACION})'[txt2]" \
    -c:a copy -map 0:a -y "$OUTPUT" 2>&1 | tail -3
  
  local SIZE=$(stat -c%s "$OUTPUT" 2>/dev/null)
  echo "   ✅ $(echo "scale=1; $SIZE/1048576" | bc)MB"
}

echo "============================================"
echo "   GENERANDO 7 VÍDEOS CON MOVIMIENTO"
echo "============================================"
echo ""

# 1. AHORRO - fondo: dinero.mp4 (man counting banknotes)
crear_video "dinero.mp4" "final_ahorro.mp4" "AHORRA CON INTELIGENCIA" 10

# 2. INVERSIONES - fondo: trading.mp4 (tablet with charts)
crear_video "trading.mp4" "final_inversiones.mp4" "INVIERTE TU DINERO" 10

# 3. SEGUROS/VIDA - fondo: negocios.mp4 (colleagues office)
crear_video "negocios.mp4" "final_seguros.mp4" "PROTEGE A LOS TUYOS" 10

# 4. SALUD - fondo: salud.mp4 (doctor)
crear_video "salud.mp4" "final_salud.mp4" "CUIDA TU SALUD" 10

# 5. HOGAR - fondo: ciudad.mp4 (city buildings)
crear_video "ciudad.mp4" "final_hogar.mp4" "TU HOGAR PROTEGIDO" 10

# 6. VIAJES - fondo: viajes.mp4 (sunset)
crear_video "viajes.mp4" "final_viajes.mp4" "VIAJA TRANQUILO" 10

# 7. ESTUDIOS - fondo: exito.mp4 (woman at desk/success)
crear_video "exito.mp4" "final_estudios.mp4" "ESTUDIA EN ESPAÑA" 10

echo ""
echo "============================================"
echo "   LISTO - VÍDEOS GENERADOS"
echo "============================================"
ls -la final_*.mp4 2>/dev/null
echo ""
echo "Tamaño total:"
du -sh final_*.mp4 2>/dev/null
