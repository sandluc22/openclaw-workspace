#!/bin/bash
# Script para mantener la app de contabilidad corriendo
cd /home/node/workspace/contabilidad/app-backend

# Matar procesos anteriores
kill $(lsof -t -i:3000) 2>/dev/null
kill $(ps aux | grep serveo | grep -v grep | awk '{print $2}') 2>/dev/null
sleep 1

# Iniciar servidor
node server.js > /tmp/contabilidad-server.log 2>&1 &
echo "Servidor iniciado en puerto 3000 (PID $!)"

# Túnel Serveo
ssh -o StrictHostKeyChecking=no -R 80:localhost:3000 serveo.net > /tmp/contabilidad-tunnel.log 2>&1 &
sleep 5
echo "Túnel iniciado"
echo "URL: $(grep -oP 'https://\S+' /tmp/contabilidad-tunnel.log | head -1)"
