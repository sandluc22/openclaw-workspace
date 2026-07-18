#!/bin/bash
BACKUP_DIR="/home/node/workspace/proyectos/BACKUPS"
LOG_FILE="$BACKUP_DIR/backup-log.txt"
mkdir -p "$BACKUP_DIR"

FECHA=$(date +%F)
HORA=$(date +%H:%M)

echo "[$(date)] Iniciando backup diario..." >> "$LOG_FILE"

RESUMEN=""
TOTAL_SIZE=0
TOTAL_FILES=0

for par in "CFG:/home/node/workspace/proyectos/CFG" "Club-Contable:/home/node/workspace/proyectos/Club Contable" "Fiverr:/home/node/workspace/proyectos/Fiverr" "codigo-CFG:/home/node/workspace/cfg-restauracion"; do
    nombre="${par%%:*}"
    origen="${par##*:}"
    destino="$BACKUP_DIR/$nombre-$FECHA.tar.gz"
    
    if [ -d "$origen" ]; then
        tar czf "$destino" -C "$(dirname "$origen")" "$(basename "$origen")" 2>/dev/null
        if [ $? -eq 0 ]; then
            SIZE=$(stat -c%s "$destino" 2>/dev/null || echo 0)
            FILES=$(tar tzf "$destino" 2>/dev/null | wc -l)
            TOTAL_SIZE=$((TOTAL_SIZE + SIZE))
            TOTAL_FILES=$((TOTAL_FILES + FILES))
            SIZE_KB=$((SIZE / 1024))
            RESUMEN="$RESUMEN"$'\n'"✅ $nombre: ${SIZE_KB}KB ($FILES archivos)"
            echo "[$(date)] OK $nombre: ${SIZE}bytes" >> "$LOG_FILE"
        else
            RESUMEN="$RESUMEN"$'\n'"❌ $nombre: ERROR"
            echo "[$(date)] ERROR $nombre" >> "$LOG_FILE"
        fi
    fi
done

# Limpiar backups >30 días
BORRADOS=0
for f in "$BACKUP_DIR"/*.tar.gz; do
    if [ -f "$f" ] && [ -f "$f" ] && [ $(stat -c%Y "$f") -lt $(date -d '30 days ago' +%s) ]; then
        rm -f "$f"
        BORRADOS=$((BORRADOS + 1))
    fi
done

TOTAL_KB=$((TOTAL_SIZE / 1024))
MENSAJE="📦 Backup diario $FECHA a las $HORA$RESUMEN"$'\n\n'"🗑 Eliminados: $BORRADOS antiguos"$'\n'"📊 Total: ${TOTAL_KB}KB / $TOTAL_FILES archivos"

# Enviar a Telegram
curl -s -X POST "https://api.telegram.org/bot8181379894:AAHhMXpRWDAyN_2_r6GUCMHTREvL4D2iZWs/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\":\"7890204626\", \"text\":\"$MENSAJE\"}" > /dev/null 2>&1

echo "[$(date)] Backup completado. $TOTAL_FILES archivos, ${TOTAL_KB}KB" >> "$LOG_FILE"
