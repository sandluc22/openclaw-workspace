#!/bin/bash
# Script para iniciar la app de contabilidad
# Inicia servidor Node.js + túnel Cloudflare (sin página de advertencia)

cd /home/node/workspace/contabilidad/app-backend

# Matar procesos anteriores
kill $(lsof -t -i:3000) 2>/dev/null
kill $(ps aux | grep cloudflared | grep -v grep | awk '{print $2}') 2>/dev/null
sleep 1

# Iniciar servidor Node.js
node server.js > /tmp/contabilidad-server.log 2>&1 &
echo "✅ Servidor iniciado en puerto 3000 (PID $!)"

# Iniciar túnel Cloudflare
nohup /tmp/cloudflared tunnel --url http://localhost:3000 > /tmp/contabilidad-tunnel.log 2>&1 &
sleep 8

# Obtener URL
URL=$(grep -oP 'https://[\w-]+\.trycloudflare\.com' /tmp/contabilidad-tunnel.log | head -1)
echo ""
echo "🌐 App disponible en:"
echo "   $URL"
echo ""
echo "⚠️  La URL cambia cada vez que se reinicia el túnel."
echo "   Para mantenerla fija necesitas un dominio propio."
