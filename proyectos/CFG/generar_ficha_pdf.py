#!/usr/bin/env python3
"""Genera ficha completa de CFG Seguros en HTML y luego a PDF"""

import os

OUTDIR = "/home/node/workspace/proyectos/CFG"
HTML_PATH = os.path.join(OUTDIR, "FICHA_COMPLETA.html")
PDF_PATH = os.path.join(OUTDIR, "FICHA_CFG_SEGUROS.pdf")

# Contenido de la ficha
html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Noto Sans', sans-serif; color: #1e293b; background: #f8fafc; padding: 40px; }
h1 { font-size: 28px; color: #0f172a; border-bottom: 4px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 30px; }
h2 { font-size: 20px; color: #0f172a; background: #e0f2fe; padding: 10px 16px; border-radius: 8px; margin: 30px 0 16px 0; border-left: 5px solid #0ea5e9; }
h3 { font-size: 16px; color: #0f172a; margin: 18px 0 8px 0; padding-left: 10px; border-left: 3px solid #0ea5e9; }
table { width: 100%; border-collapse: collapse; margin: 12px 0 20px 0; font-size: 14px; }
th { text-align: left; background: #0f172a; color: white; padding: 10px 12px; }
td { padding: 8px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
td:first-child { font-weight: 700; width: 200px; color: #334155; }
tr:nth-child(even) td { background: #f1f5f9; }
.tag { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 700; }
.tag-ok { background: #dcfce7; color: #166534; }
.tag-pen { background: #fef9c3; color: #854d0e; }
.tag-warn { background: #fee2e2; color: #991b1b; }
.section { background: white; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
ul { margin: 8px 0 8px 20px; font-size: 14px; line-height: 1.8; }
li { margin-bottom: 4px; }
.code { background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-size: 13px; }
</style>
</head>
<body>

<h1>📋 FICHA COMPLETA — CFG SEGUROS</h1>
<p style="font-size:14px;color:#64748b;margin-bottom:30px">Última actualización: 18 julio 2026</p>

<!-- 1. DATOS GENERALES -->
<div class="section">
<h2>1. DATOS GENERALES</h2>
<table>
  <tr><td>Nombre comercial</td><td>CFG Seguros</td></tr>
  <tr><td>Nombre redes</td><td>CFG-Seguros (con guión)</td></tr>
  <tr><td>Grupo</td><td>Grupo Galilea</td></tr>
  <tr><td>Rol</td><td>Colaborador de Grupo Galilea · Correduría de seguros</td></tr>
  <tr><td>Titular legal</td><td>CFG Seguros</td></tr>
  <tr><td>Email</td><td>info@cfg-seguros.com</td></tr>
  <tr><td>Email ventas</td><td>ventas@cfg-seguros.com</td></tr>
  <tr><td>Teléfono WhatsApp</td><td>+34 641 75 44 90</td></tr>
  <tr><td>Web</td><td>https://cfg-seguros.com</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-ok">✅ Activo y operativo</span></td></tr>
</table>
</div>

<!-- 2. WEB -->
<div class="section">
<h2>2. WEB — cfg-seguros.com</h2>
<table>
  <tr><td>Dominio</td><td>cfg-seguros.com</td></tr>
  <tr><td>Hosting</td><td>Cloudflare Pages (proyecto cfg-seguros-web)</td></tr>
  <tr><td>URL pages.dev</td><td>https://cfg-seguros-web.pages.dev</td></tr>
  <tr><td>SSL</td><td><span class="tag tag-ok">✅ Activo (Cloudflare)</span></td></tr>
  <tr><td>Rama producción</td><td>master</td></tr>
  <tr><td>Deploy</td><td><span class="tag tag-ok">✅ Automático desde GitHub</span></td></tr>
  <tr><td>Formulario</td><td>Web3Forms → leads a info@cfg-seguros.com + Telegram</td></tr>
  <tr><td>WhatsApp flotante</td><td><span class="tag tag-ok">✅ Botón verde abajo derecha → wa.me/+34641754490</span></td></tr>
  <tr><td>Google Search Console</td><td><span class="tag tag-ok">✅ Verificado (sandluc22@gmail.com)</span></td></tr>
  <tr><td>Google Business Profile</td><td><span class="tag tag-pen">⏳ En revisión (esperando carta física)</span></td></tr>
</table>

<h3>📄 Páginas del sitio (16)</h3>
<table>
  <tr><th>Ruta</th><th>Descripción</th></tr>
  <tr><td class="code">/index.html</td><td>Home · Presentación + servicios + blog + formulario</td></tr>
  <tr><td class="code">/privacidad.html</td><td>Política de Privacidad</td></tr>
  <tr><td class="code">/aviso-legal.html</td><td>Aviso Legal</td></tr>
  <tr><td class="code">/seguros/index.html</td><td>Listado de seguros</td></tr>
  <tr><td class="code">/seguros/vida.html</td><td>Seguro de Vida</td></tr>
  <tr><td class="code">/seguros/salud.html</td><td>Seguro de Salud</td></tr>
  <tr><td class="code">/seguros/hogar.html</td><td>Seguro de Hogar</td></tr>
  <tr><td class="code">/seguros/coche.html</td><td>Seguro de Coche</td></tr>
  <tr><td class="code">/seguros/empresas.html</td><td>Seguro de Empresas</td></tr>
  <tr><td class="code">/seguros/ahorro-inversion.html</td><td>Plan de Ahorro e Inversión</td></tr>
  <tr><td class="code">/blog/index.html</td><td>Blog principal</td></tr>
  <tr><td class="code">/blog/seguro-vida-mitos-realidades.html</td><td>Seguro de vida: mitos y realidades</td></tr>
  <tr><td class="code">/blog/seguro-salud-guia-completa.html</td><td>Guía completa del seguro de salud</td></tr>
  <tr><td class="code">/blog/proteccion-empresas-autonomos.html</td><td>Protección financiera empresas y autónomos</td></tr>
  <tr><td class="code">/blog/ahorro-inversion-primeros-pasos.html</td><td>Ahorro e inversión: primeros pasos</td></tr>
  <tr><td class="code">/referencia-crecimientofinancieroglobal.html</td><td>Redirección desde antiguo dominio</td></tr>
</table>

<h3>🎨 Logos y assets</h3>
<table>
  <tr><td>Logo PNG</td><td class="code">/home/node/workspace/cfg-seguros/logo-cfg-seguros.png</td></tr>
  <tr><td>Logo SVG</td><td class="code">/home/node/workspace/cfg-seguros/logo-cfg-seguros.svg</td></tr>
  <tr><td>Favicon</td><td>No tiene favicon configurado</td></tr>
</table>
</div>

<!-- 3. GITHUB -->
<div class="section">
<h2>3. GITHUB — sandluc22/cfg-seguros</h2>
<table>
  <tr><td>Repositorio</td><td>https://github.com/sandluc22/cfg-seguros</td></tr>
  <tr><td>Rama principal</td><td>master (producción)</td></tr>
  <tr><td>Deploy a Cloudflare</td><td><span class="tag tag-ok">✅ Automático</span></td></tr>
  <tr><td>Últimos commits</td><td>Footer limpio, iconos redes redondos, WhatsApp, LinkedIn, TikTok</td></tr>
  <tr><td>Token GitHub</td><td class="code">/home/node/workspace/.creds/github.json</td></tr>
</table>
</div>

<!-- 4. REDES SOCIALES -->
<div class="section">
<h2>4. REDES SOCIALES</h2>

<h3>📷 Instagram — @cfg_seguros_gg</h3>
<table>
  <tr><td>Usuario</td><td>@cfg_seguros_gg</td></tr>
  <tr><td>URL</td><td>https://www.instagram.com/cfg_seguros_gg/</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-ok">✅ Creada y operativa</span></td></tr>
  <tr><td>Posts preparados</td><td>7 posts (carpeta proyectos/CFG/redes/instagram/)</td></tr>
  <tr><td>Post lanzamiento</td><td><span class="tag tag-ok">✅ Publicado</span></td></tr>
</table>

<h3>📘 Facebook — CFG Seguros</h3>
<table>
  <tr><td>URL</td><td>https://www.facebook.com/profile.php?id=61591242009330</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-ok">✅ Creada y operativa</span></td></tr>
  <tr><td>WhatsApp conectado</td><td><span class="tag tag-ok">✅ Integrado</span></td></tr>
  <tr><td>Posts preparados</td><td>7 posts (carpeta proyectos/CFG/redes/facebook/)</td></tr>
  <tr><td>Imágenes generadas</td><td>7 imágenes PNG con Noto Sans, sin precios, con correo</td></tr>
</table>

<h3>💼 LinkedIn — cfg-seguros</h3>
<table>
  <tr><td>URL</td><td>https://www.linkedin.com/company/cfg-seguros</td></tr>
  <tr><td>Nombre página</td><td>cfg-seguros</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-ok">✅ Creada</span></td></tr>
  <tr><td>Logo</td><td><span class="tag tag-ok">✅ Subido</span></td></tr>
  <tr><td>Banner</td><td><span class="tag tag-ok">✅ Generado (1128x191px)</span></td></tr>
  <tr><td>Botón personalizado</td><td>Enlace a cfg-seguros.com</td></tr>
  <tr><td>Posts preparados</td><td>3 posts (Presentación, Ahorro, Corredor vs Agente)</td></tr>
  <tr><td>Imágenes generadas</td><td>3 imágenes cuadradas 1080x1080</td></tr>
</table>

<h3>🎵 TikTok — @cfgsegurosgg</h3>
<table>
  <tr><td>Usuario</td><td>@cfgsegurosgg</td></tr>
  <tr><td>URL</td><td>https://www.tiktok.com/@cfgsegurosgg</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-ok">✅ Creada</span></td></tr>
  <tr><td>Logo</td><td><span class="tag tag-ok">✅ Subido</span></td></tr>
  <tr><td>Bio</td><td>CFG-Seguros · Colaborador Grupo Galilea · Seguros</td></tr>
  <tr><td>Website</td><td>cfg-seguros.com</td></tr>
  <tr><td>Vídeos subidos</td><td>2 vídeos (errores coche + seguro hogar, 18s cada uno)</td></tr>
</table>

<h3>📋 Posts por red — Resumen</h3>
<table>
  <tr><th>Red</th><th>Posts</th><th>Frecuencia</th></tr>
  <tr><td>Instagram</td><td>7 posts (imágenes cuadradas)</td><td>Lun/Mié/Vie</td></tr>
  <tr><td>Facebook</td><td>7 posts adaptados de IG</td><td>Lun/Mié/Vie</td></tr>
  <tr><td>LinkedIn</td><td>3 posts (tono profesional)</td><td>Lun/Mié/Vie</td></tr>
  <tr><td>TikTok</td><td>2 vídeos subidos</td><td>Cuando puedas grabar más</td></tr>
</table>
</div>

<!-- 5. INFRAESTRUCTURA TÉCNICA -->
<div class="section">
<h2>5. INFRAESTRUCTURA TÉCNICA</h2>
<table>
  <tr><td>DNS</td><td>Cloudflare</td></tr>
  <tr><td>Zone ID</td><td class="code">9986e3c1cb4dd72f25ba56ec9afdb727</td></tr>
  <tr><td>Account ID</td><td class="code">72305fb85467e89da2940e359f9e09cc</td></tr>
  <tr><td>Hosting web</td><td>Cloudflare Pages (proyecto cfg-seguros-web)</td></tr>
  <tr><td>Formulario</td><td>Web3Forms</td></tr>
  <tr><td>Correos</td><td>Migadu (info@cfg-seguros.com, ventas@cfg-seguros.com)</td></tr>
  <tr><td>Repositorio</td><td>GitHub sandluc22/cfg-seguros (rama master)</td></tr>
  <tr><td>Deploy automático</td><td><span class="tag tag-ok">✅ GitHub → Cloudflare Pages</span></td></tr>
  <tr><td>Token Cloudflare</td><td class="code">/home/node/workspace/.creds/cloudflare.json</td></tr>
  <tr><td>SSL</td><td><span class="tag tag-ok">✅ Flexible (Cloudflare)</span></td></tr>
</table>
</div>

<!-- 6. CONTENIDO WEB -->
<div class="section">
<h2>6. CONTENIDO Y ESTILO WEB</h2>
<table>
  <tr><td>Footer</td><td>Email, Blog, Seguros, Privacidad, Aviso Legal, ©2026</td></tr>
  <tr><td>Sección redes</td><td>Iconos redondos: Instagram, Facebook, LinkedIn, TikTok</td></tr>
  <tr><td>WhatsApp flotante</td><td>Botón verde abajo derecha en todas las páginas</td></tr>
  <tr><td>Colaboración</td><td>"Protege lo que importa — Colaborador de Grupo Galilea"</td></tr>
  <tr><td>CTA en posts</td><td>📧 info@cfg-seguros.com</td></tr>
  <tr><td>Restricción posts</td><td>Sin mencionar precios, sin "Unit Linked"</td></tr>
  <tr><td>Fuente imágenes</td><td>Noto Sans (ñ y acentos correctos)</td></tr>
  <tr><td>Imágenes posts</td><td>Unsplash (fotos reales, profesionales)</td></tr>
</table>
</div>

<!-- 7. CORREOS -->
<div class="section">
<h2>7. CORREOS ELECTRÓNICOS</h2>
<table>
  <tr><td>Proveedor</td><td>Migadu</td></tr>
  <tr><td>info@cfg-seguros.com</td><td><span class="tag tag-ok">✅ Funcionando</span></td></tr>
  <tr><td>ventas@cfg-seguros.com</td><td><span class="tag tag-ok">✅ Funcionando</span></td></tr>
  <tr><td>info@crecimientofinancieroglobal.com</td><td><span class="tag tag-ok">✅ Funcionando</span></td></tr>
</table>
</div>

<!-- 8. GOOGLE -->
<div class="section">
<h2>8. GOOGLE</h2>
<table>
  <tr><td>Search Console</td><td><span class="tag tag-ok">✅ Dominio cfg-seguros.com verificado</span></td></tr>
  <tr><td>Cuenta</td><td>crecimientofinancieroglobal@gmail.com / sandluc22@gmail.com</td></tr>
  <tr><td>Tráfico orgánico</td><td>0 tráfico real (sitio nuevo, < 1 semana)</td></tr>
  <tr><td>Impresiones Google</td><td>3 impresiones (posiblemente visitas propias)</td></tr>
  <tr><td>Business Profile</td><td><span class="tag tag-pen">⏳ En revisión (esperando carta física)</span></td></tr>
</table>
</div>

<!-- 9. PROYECTO ANTERIOR -->
<div class="section">
<h2>9. PROYECTO ANTERIOR — Crecimiento Financiero Global</h2>
<table>
  <tr><td>Web</td><td>crecimientofinancieroglobal.com</td></tr>
  <tr><td>Estado</td><td><span class="tag tag-warn">⏸️ APARCADO</span></td></tr>
  <tr><td>Hosting</td><td>Cloudflare Worker (yellow-bar-eceb)</td></tr>
  <tr><td>Nota</td><td>Formulario no funcional. No tocar. El proyecto vivo es cfg-seguros.com</td></tr>
</table>
</div>

<!-- 10. PENDIENTES -->
<div class="section">
<h2>10. PENDIENTES</h2>
<table>
  <tr><th>#</th><th>Tarea</th><th>Estado</th></tr>
  <tr><td>1</td><td>Google Business Profile (esperar carta física y verificar)</td><td><span class="tag tag-pen">⏳</span></td></tr>
  <tr><td>2</td><td>Publicar posts en Instagram, Facebook y LinkedIn (lun/mié/vie)</td><td><span class="tag tag-pen">⏳</span></td></tr>
  <tr><td>3</td><td>Configurar Supervisor (chatbot WhatsApp con conocimiento CFG Seguros)</td><td><span class="tag tag-pen">⏳</span></td></tr>
  <tr><td>4</td><td>Más vídeos TikTok (grabar con móvil, yo preparo guiones)</td><td><span class="tag tag-pen">⏳</span></td></tr>
  <tr><td>5</td><td>Favicon para la web</td><td><span class="tag tag-pen">⏳</span></td></tr>
  <tr><td>6</td><td>Seguir escribiendo artículos de blog</td><td><span class="tag tag-pen">⏳</span></td></tr>
</table>
</div>

<!-- 11. UBICACIÓN EN WORKSPACE -->
<div class="section">
<h2>11. UBICACIÓN EN WORKSPACE</h2>
<table>
  <tr><th>Carpeta</th><th>Contenido</th></tr>
  <tr><td class="code">/home/node/workspace/cfg-seguros/</td><td>Web completa (16 HTML + logos + assets)</td></tr>
  <tr><td class="code">/home/node/workspace/proyectos/CFG/redes/</td><td>Redes sociales (instagram, facebook, linkedin, tiktok)</td></tr>
  <tr><td class="code">/home/node/workspace/proyectos/CFG/redes/facebook/imagenes/</td><td>7 imágenes posts Facebook</td></tr>
  <tr><td class="code">/home/node/workspace/proyectos/CFG/redes/linkedin/imagenes/</td><td>3 imágenes posts LinkedIn + banner</td></tr>
  <tr><td class="code">/home/node/workspace/proyectos/CFG/redes/tiktok/</td><td>2 vídeos TikTok + frames</td></tr>
  <tr><td class="code">/home/node/workspace/proyectos/CFG/FICHA.md</td><td>Ficha resumen CFG</td></tr>
  <tr><td class="code">/home/node/workspace/SEGUIR_CON_SANDRA/CFG.md</td><td>Ficha de seguimiento diario</td></tr>
  <tr><td class="code">/home/node/workspace/memory/2026-07-18.md</td><td>Diario del día</td></tr>
  <tr><td class="code">/home/node/workspace/MEMORY.md</td><td>Memoria permanente (todo el historial)</td></tr>
  <tr><td class="code">/home/node/workspace/.creds/</td><td>Credenciales (Cloudflare, GitHub)</td></tr>
</table>
</div>

<!-- 12. RECORDATORIOS -->
<div class="section">
<h2>12. RECORDATORIOS ACTIVOS (CRON)</h2>
<table>
  <tr><th>Hora (España)</th><th>Qué hace</th></tr>
  <tr><td>6:30 (lun/vie)</td><td>Saludo diario con tareas pendientes</td></tr>
  <tr><td>6:30 (lun/mié/vie)</td><td>Publicar en redes (IG, FB, LinkedIn)</td></tr>
  <tr><td>22:30 (diario)</td><td>Cierre del día: guardar diario + enviar resumen</td></tr>
</table>
</div>

<hr style="margin: 40px 0; border: none; border-top: 2px solid #e2e8f0;">
<p style="text-align:center;font-size:13px;color:#94a3b8;">
Ficha generada por Alfa · 18 julio 2026 · CFG Seguros
</p>

</body>
</html>'''

# Escribir HTML
os.makedirs(OUTDIR, exist_ok=True)
with open(HTML_PATH, "w") as f:
    f.write(html)
print(f"✅ HTML creado: {HTML_PATH}")

# Convertir a PDF
os.system(f"wkhtmltopdf --encoding UTF-8 '{HTML_PATH}' '{PDF_PATH}' 2>&1 | tail -5")
print(f"\n✅ PDF creado: {PDF_PATH}")
