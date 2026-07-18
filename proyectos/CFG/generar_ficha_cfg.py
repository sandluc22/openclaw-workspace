#!/usr/bin/env python3
"""Genera FICHA TÉCNICA de CFG Seguros actualizada"""

import os

OUTDIR = "/home/node/workspace/proyectos/CFG"
HTML_PATH = os.path.join(OUTDIR, "FICHA_COMPLETA_CFG_SEGUROS.html")
PDF_PATH = os.path.join(OUTDIR, "FICHA_CFG_SEGUROS.pdf")

html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Noto Sans', sans-serif; color: #1e293b; background: #f8fafc; padding: 40px; }
h1 { font-size: 28px; color: #0f172a; border-bottom: 4px solid #0ea5e9; padding-bottom: 12px; margin-bottom: 8px; }
h2 { font-size: 18px; color: #0f172a; background: #e0f2fe; padding: 8px 14px; border-radius: 6px; margin: 28px 0 12px 0; border-left: 4px solid #0ea5e9; }
.subtitle { font-size: 13px; color: #64748b; margin-bottom: 30px; }
table { width: 100%; border-collapse: collapse; margin: 10px 0 18px 0; font-size: 13px; }
th { text-align: left; background: #0f172a; color: white; padding: 8px 10px; font-size: 12px; }
td { padding: 6px 10px; border-bottom: 1px solid #e2e8f0; vertical-align: top; font-size: 13px; }
td:first-child { font-weight: 700; width: 200px; color: #334155; background: #f1f5f9; }
tr:nth-child(even) td:first-child { background: #e9edf2; }
.tag-ok { color: #166534; background: #dcfce7; padding: 2px 8px; border-radius: 10px; font-size: 11px; display: inline-block; }
.tag-pen { color: #854d0e; background: #fef9c3; padding: 2px 8px; border-radius: 10px; font-size: 11px; display: inline-block; }
.tag-warn { color: #991b1b; background: #fee2e2; padding: 2px 8px; border-radius: 10px; font-size: 11px; display: inline-block; }
.code { font-family: monospace; font-size: 12px; background: #f1f5f9; padding: 1px 5px; border-radius: 3px; }
.section { background: white; border-radius: 10px; padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
hr { margin: 30px 0; border: none; border-top: 2px solid #e2e8f0; }
.footer { text-align: center; font-size: 12px; color: #94a3b8; margin-top: 30px; }
</style>
</head>
<body>

<h1>FICHA TÉCNICA — CFG Seguros</h1>
<div class="subtitle">Propietaria: Sandra Caicedo · Última actualización: 18-jul-2026</div>

<!-- 1. DOMINIO -->
<div class="section">
<h2>1. DOMINIO</h2>
<table>
  <tr><td>Dato</td><td>Valor</td></tr>
  <tr><td>Dominio</td><td>cfg-seguros.com</td></tr>
  <tr><td>Registrado en</td><td>Porkbun</td></tr>
  <tr><td>Email de la cuenta</td><td>crecimientofinancieroglobal@gmail.com</td></tr>
  <tr><td>Contraseña Porkbun</td><td>Sandra.1982</td></tr>
  <tr><td>API Key Porkbun</td><td>pk1_4a757ee2394d97598093b61ab86e45e5898cff6d91f675850fce8f67b31f45fe</td></tr>
  <tr><td>Secret API Key</td><td>sk1_ce778b843bbc9e919e3cee418f331e55af6ac7e43e19ab01858c35699bf65776</td></tr>
  <tr><td>Fecha de creación</td><td>~10-jul-2026</td></tr>
  <tr><td>Fecha de expiración</td><td>Pendiente de verificar en Porkbun</td></tr>
  <tr><td>Precio/año</td><td>Pendiente de verificar</td></tr>
</table>
</div>

<!-- 2. HOSTING -->
<div class="section">
<h2>2. HOSTING / DÓNDE ESTÁ SUBIDA LA WEB</h2>
<table>
  <tr><td>Plataforma</td><td>Estado</td><td>URL</td><td>Notas</td></tr>
  <tr><td>Cloudflare Pages</td><td><span class="tag-ok">Activo</span></td><td>cfg-seguros.com</td><td>Proyecto cfg-seguros-web</td></tr>
  <tr><td>URL pages.dev</td><td>—</td><td>cfg-seguros-web.pages.dev</td><td>URL de desarrollo</td></tr>
</table>
<h3>Acceso Cloudflare</h3>
<table>
  <tr><td>Account ID</td><td class="code">72305fb85467e89da2940e359f9e09cc</td></tr>
  <tr><td>Zone ID</td><td class="code">9986e3c1cb4dd72f25ba56ec9afdb727</td></tr>
  <tr><td>Token Pages</td><td class="code">cfut_z79y6120YMMJkXpIYWrWKPH2rwdJdoS8i4XP1u3e921ce861</td></tr>
  <tr><td>Email Cloudflare</td><td>crecimientofinancieroglobal@gmail.com</td></tr>
  <tr><td>Dashboard</td><td>https://dash.cloudflare.com</td></tr>
</table>
</div>

<!-- 3. CORREOS -->
<div class="section">
<h2>3. CORREOS</h2>
<table>
  <tr><td>Cuenta</td><td>Gestionado por</td><td>Estado</td></tr>
  <tr><td>info@cfg-seguros.com</td><td>Migadu (pago)</td><td><span class="tag-ok">Funcionando</span></td></tr>
  <tr><td>ventas@cfg-seguros.com</td><td>Migadu (pago)</td><td><span class="tag-ok">Funcionando</span></td></tr>
  <tr><td>info@crecimientofinancieroglobal.com</td><td>Migadu (pago)</td><td><span class="tag-ok">Funcionando</span></td></tr>
  <tr><td>crecimientofinancieroglobal@gmail.com</td><td>Gmail</td><td>Cuenta principal</td></tr>
  <tr><td>sandluc22@gmail.com</td><td>Gmail</td><td>Cuenta secundaria</td></tr>
</table>
<h3>Acceso Migadu</h3>
<table>
  <tr><td>Usuario</td><td>sandluc22@gmail.com</td></tr>
  <tr><td>Contraseña</td><td>AlfaySandra.</td></tr>
  <tr><td>Dashboard</td><td>https://panel.migadu.com</td></tr>
</table>
</div>

<!-- 4. DNS / IP / NAMESERVERS -->
<div class="section">
<h2>4. DNS / IP / NAMESERVERS</h2>
<table>
  <tr><td>Gestionado por</td><td>Cloudflare</td></tr>
  <tr><td>Nameservers</td><td>NS de Cloudflare</td></tr>
  <tr><td>SSL</td><td><span class="tag-ok">Activo (Flexible, Cloudflare)</span></td></tr>
  <tr><td>Registro CNAME</td><td>cfg-seguros.com → cfg-seguros-web.pages.dev</td></tr>
  <tr><td>IP/Proxy</td><td>Cloudflare proxy (naranja)</td></tr>
</table>
</div>

<!-- 5. SERVICIOS TÉCNICOS -->
<div class="section">
<h2>5. SERVICIOS TÉCNICOS</h2>
<table>
  <tr><td>Servicio</td><td>Dato</td><td>Estado</td></tr>
  <tr><td>Google Search Console</td><td>cfg-seguros.com</td><td><span class="tag-ok">Verificado</span></td></tr>
  <tr><td>Google Business Profile</td><td>CFG Seguros</td><td><span class="tag-pen">En revisión (esperando carta)</span></td></tr>
  <tr><td>Web3Forms (formulario)</td><td>Access Key configurado</td><td><span class="tag-ok">Funcionando</span></td></tr>
  <tr><td>SSL</td><td>Automático Cloudflare</td><td><span class="tag-ok">Activo</span></td></tr>
  <tr><td>WhatsApp flotante</td><td>wa.me/+34641754490</td><td><span class="tag-ok">En todas las páginas</span></td></tr>
  <tr><td>Deploy automático</td><td>GitHub → Cloudflare Pages</td><td><span class="tag-ok">Configurado</span></td></tr>
  <tr><td>Favicon</td><td>Logo CFG Seguros (favicon.ico, .png, apple-touch)</td><td><span class="tag-ok">Puesto en todas las páginas</span></td></tr>
  <tr><td>Google Analytics (GA4)</td><td>No configurado</td><td><span class="tag-pen">Pendiente</span></td></tr>
</table>
</div>

<!-- 6. PRESUPUESTO / COSTES -->
<div class="section">
<h2>6. PRESUPUESTO / COSTES</h2>
<table>
  <tr><td>Servicio</td><td>Coste</td><td>Frecuencia</td><td>Próximo pago</td></tr>
  <tr><td>Porkbun (dominio .com)</td><td>Pendiente</td><td>Anual</td><td>Pendiente</td></tr>
  <tr><td>Migadu (correos)</td><td>Pendiente</td><td>Mensual/anual</td><td>Pendiente</td></tr>
  <tr><td>Cloudflare Pages</td><td>Gratis</td><td>—</td><td>—</td></tr>
  <tr><td>Web3Forms</td><td>Gratis (plan básico)</td><td>—</td><td>—</td></tr>
  <tr><td>Google (Gmail, GSC)</td><td>Gratis</td><td>—</td><td>—</td></tr>
</table>
</div>

<!-- 7. FECHAS DE CADUCIDAD -->
<div class="section">
<h2>7. FECHAS DE CADUCIDAD</h2>
<table>
  <tr><td>Servicio</td><td>Fecha de caducidad</td><td>Alerta</td></tr>
  <tr><td>Dominio (Porkbun)</td><td>Pendiente de consultar</td><td>No configurada</td></tr>
  <tr><td>Migadu (correo)</td><td>Pendiente de consultar</td><td>No configurada</td></tr>
  <tr><td>SSL</td><td>Se renueva automáticamente</td><td>—</td></tr>
</table>
</div>

<!-- 8. REDES SOCIALES -->
<div class="section">
<h2>8. REDES SOCIALES</h2>
<table>
  <tr><th>Red</th><th>Usuario/URL</th><th>Posts</th><th>Estado</th></tr>
  <tr><td>Instagram</td><td>@cfg_seguros_gg</td><td>7 imágenes</td><td><span class="tag-ok">Activa · Post lanzamiento publicado</span></td></tr>
  <tr><td>Facebook</td><td>profile.php?id=61591242009330</td><td>7 imágenes</td><td><span class="tag-ok">Activa · WhatsApp integrado</span></td></tr>
  <tr><td>LinkedIn</td><td>company/cfg-seguros</td><td>3 imágenes + banner</td><td><span class="tag-ok">Activa</span></td></tr>
  <tr><td>TikTok</td><td>@cfgsegurosgg</td><td>2 vídeos subidos</td><td><span class="tag-ok">Creada</span></td></tr>
</table>
</div>

<!-- 9. INFRAESTRUCTURA TÉCNICA -->
<div class="section">
<h2>9. INFRAESTRUCTURA TÉCNICA</h2>
<table>
  <tr><td>Concepto</td><td>Detalle</td></tr>
  <tr><td>Repositorio GitHub</td><td>github.com/sandluc22/cfg-seguros (rama master)</td></tr>
  <tr><td>Deploy</td><td>Automático: GitHub → Cloudflare Pages</td></tr>
  <tr><td>Formulario leads</td><td>Web3Forms → info@cfg-seguros.com + Telegram</td></tr>
  <tr><td>Código fuente</td><td>/home/node/workspace/cfg-seguros/</td></tr>
  <tr><td>Logos</td><td>logo-cfg-seguros.png, .svg, .real.svg</td></tr>
  <tr><td>Posts redes</td><td>/home/node/workspace/proyectos/CFG/redes/</td></tr>
  <tr><td>Vídeos TikTok</td><td>/home/node/workspace/proyectos/CFG/redes/tiktok/</td></tr>
  <tr><td>Ficha técnica PDF</td><td>/home/node/workspace/proyectos/CFG/FICHA_CFG_SEGUROS.pdf</td></tr>
</table>
</div>

<!-- 10. PÁGINAS DE LA WEB -->
<div class="section">
<h2>10. PÁGINAS DE LA WEB</h2>
<table>
  <tr><th>Página</th><th>Archivo</th></tr>
  <tr><td>Home</td><td class="code">index.html</td></tr>
  <tr><td>Política de Privacidad</td><td class="code">privacidad.html</td></tr>
  <tr><td>Aviso Legal</td><td class="code">aviso-legal.html</td></tr>
  <tr><td>Seguros (listado)</td><td class="code">seguros/index.html</td></tr>
  <tr><td>Seguro de Vida</td><td class="code">seguros/vida.html</td></tr>
  <tr><td>Seguro de Salud</td><td class="code">seguros/salud.html</td></tr>
  <tr><td>Seguro de Hogar</td><td class="code">seguros/hogar.html</td></tr>
  <tr><td>Seguro de Coche</td><td class="code">seguros/coche.html</td></tr>
  <tr><td>Seguro de Empresas</td><td class="code">seguros/empresas.html</td></tr>
  <tr><td>Plan de Ahorro e Inversión</td><td class="code">seguros/ahorro-inversion.html</td></tr>
  <tr><td>Blog principal</td><td class="code">blog/index.html</td></tr>
  <tr><td>Seguro de Vida: mitos y realidades</td><td class="code">blog/seguro-vida-mitos-realidades.html</td></tr>
  <tr><td>Guía completa seguro de salud</td><td class="code">blog/seguro-salud-guia-completa.html</td></tr>
  <tr><td>Protección empresas y autónomos</td><td class="code">blog/proteccion-empresas-autonomos.html</td></tr>
  <tr><td>Ahorro e inversión: primeros pasos</td><td class="code">blog/ahorro-inversion-primeros-pasos.html</td></tr>
  <tr><td>Redirección CFG Global</td><td class="code">referencia-crecimientofinancieroglobal.html</td></tr>
  <tr><td>Favicon</td><td class="code">favicon.ico, favicon.png, apple-touch-icon.png</td></tr>
  <tr><td>Logos</td><td class="code">logo-cfg-seguros.png, .svg, .real.svg</td></tr>
</table>
</div>

<!-- 11. TAREAS PENDIENTES -->
<div class="section">
<h2>11. TAREAS PENDIENTES</h2>
<table>
  <tr><th>#</th><th>Tarea</th><th>Estado</th></tr>
  <tr><td>1</td><td>Verificar Google Business Profile (esperar carta física)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>2</td><td>Publicar posts en redes (lun/mié/vie — IG, FB, LinkedIn)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>3</td><td>Configurar Supervende (chatbot WhatsApp con conocimiento CFG)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>4</td><td>Más vídeos para TikTok (grabar con móvil)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>5</td><td>Más artículos para el blog</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>6</td><td>Configurar Google Analytics (GA4)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>7</td><td>Verificar fechas de caducidad (dominio, Migadu)</td><td><span class="tag-pen">⏳</span></td></tr>
  <tr><td>8</td><td>Verificar coste de Migadu y próxima factura</td><td><span class="tag-pen">⏳</span></td></tr>
</table>
</div>

<!-- 12. CONTRASEÑAS -->
<div class="section">
<h2>12. RESUMEN DE CONTRASEÑAS</h2>
<table>
  <tr><td>Sitio</td><td>Email</td><td>Nota</td></tr>
  <tr><td>Porkbun</td><td>crecimientofinancieroglobal@gmail.com</td><td>Contraseña: Sandra.1982</td></tr>
  <tr><td>Gmail CFG</td><td>crecimientofinancieroglobal@gmail.com</td><td>Contraseña: Slch12345+</td></tr>
  <tr><td>Gmail personal</td><td>sandluc22@gmail.com</td><td>Cuenta secundaria</td></tr>
  <tr><td>Cloudflare</td><td>crecimientofinancieroglobal@gmail.com</td><td>Token en .creds/cloudflare.json</td></tr>
  <tr><td>Migadu</td><td>sandluc22@gmail.com</td><td>Contraseña: AlfaySandra.</td></tr>
  <tr><td>Netlify</td><td>crecimientofinancieroglobal@gmail.com</td><td>Login con Google</td></tr>
  <tr><td>GitHub</td><td>sandluc22</td><td>Token en .creds/github.json</td></tr>
  <tr><td>Surge</td><td>crecimientofinancieroglobal@gmail.com</td><td>Contraseña: Alfa.1982</td></tr>
</table>
</div>

<!-- 13. REGISTRO DE CAMBIOS -->
<div class="section">
<h2>13. REGISTRO DE CAMBIOS</h2>
<table>
  <tr><th>Fecha</th><th>Cambio</th></tr>
  <tr><td>~10-jul-2026</td><td>Creación dominio cfg-seguros.com. Web montada en Cloudflare Pages.</td></tr>
  <tr><td>~12-jul-2026</td><td>Formulario Web3Forms configurado. Correos Migadu activos.</td></tr>
  <tr><td>14-jul-2026</td><td>Google Search Console verificado. Blog con 4 artículos.</td></tr>
  <tr><td>14-jul-2026</td><td>Instagram @cfg_seguros_gg creado y post de lanzamiento publicado.</td></tr>
  <tr><td>18-jul-2026</td><td>Facebook: 7 posts + WhatsApp integrado + Privacidad + Aviso Legal.</td></tr>
  <tr><td>18-jul-2026</td><td>LinkedIn: página creada, 3 posts, banner, botón personalizado.</td></tr>
  <tr><td>18-jul-2026</td><td>TikTok: cuenta @cfgsegurosgg creada, logo, 2 vídeos subidos.</td></tr>
  <tr><td>18-jul-2026</td><td>Web: footer limpio, iconos redes redondos, WhatsApp flotante.</td></tr>
  <tr><td>18-jul-2026</td><td>Deploy automático GitHub → Cloudflare Pages configurado.</td></tr>
  <tr><td>18-jul-2026</td><td>Favicon añadido a todas las páginas (logo en pestaña navegador).</td></tr>
  <tr><td>18-jul-2026</td><td>Ficha técnica PDF generada y actualizada.</td></tr>
</table>
</div>

<!-- 14. ARCHIVOS DEL PROYECTO -->
<div class="section">
<h2>14. ARCHIVOS DEL PROYECTO</h2>
<table>
  <tr><td>Archivo</td><td>Ruta</td></tr>
  <tr><td>Código fuente web</td><td class="code">/home/node/workspace/cfg-seguros/</td></tr>
  <tr><td>Logos</td><td class="code">cfg-seguros/logo-cfg-seguros.png, .svg, .real.svg</td></tr>
  <tr><td>Favicon</td><td class="code">cfg-seguros/favicon.ico, favicon.png, apple-touch-icon.png</td></tr>
  <tr><td>Posts Instagram</td><td class="code">proyectos/CFG/redes/instagram/POSTS.md</td></tr>
  <tr><td>Posts Facebook</td><td class="code">proyectos/CFG/redes/facebook/POSTS.md + imágenes/</td></tr>
  <tr><td>Posts LinkedIn</td><td class="code">proyectos/CFG/redes/linkedin/POSTS.md + imágenes/ + banner</td></tr>
  <tr><td>Vídeos TikTok</td><td class="code">proyectos/CFG/redes/tiktok/*.mp4</td></tr>
  <tr><td>Ficha técnica (PDF)</td><td class="code">proyectos/CFG/FICHA_CFG_SEGUROS.pdf</td></tr>
  <tr><td>Seguimiento diario</td><td class="code">SEGUIR_CON_SANDRA/CFG.md</td></tr>
  <tr><td>Diario del día</td><td class="code">memory/2026-07-18.md</td></tr>
  <tr><td>Memoria permanente</td><td class="code">MEMORY.md</td></tr>
  <tr><td>Credenciales Cloudflare</td><td class="code">.creds/cloudflare.json</td></tr>
  <tr><td>Credenciales GitHub</td><td class="code">.creds/github.json</td></tr>
  <tr><td>Generador ficha PDF</td><td class="code">proyectos/CFG/generar_ficha_cfg.py</td></tr>
</table>
</div>

<!-- 15. INSTRUCCIONES DE RECUPERACIÓN -->
<div class="section">
<h2>15. INSTRUCCIONES DE RECUPERACIÓN</h2>
<p style="font-size:13px;line-height:1.8">
Si todo se pierde:<br>
1. Clonar repositorio: <span class="code">git clone https://github.com/sandluc22/cfg-seguros.git</span><br>
2. GitHub → Cloudflare Pages: reconnect desde el panel (necesita autorización OAuth manual)<br>
3. SSL: Cloudflare lo genera automáticamente<br>
4. Correos: info@ y ventas@ ya configurados en Migadu<br>
5. Formulario: Web3Forms ya tiene el access_key en el código HTML<br>
6. Redes sociales: todas las contraseñas en CONTRASEÑAS/ y en esta ficha
</p>
</div>

<!-- 16. NOTAS IMPORTANTES -->
<div class="section">
<h2>NOTAS IMPORTANTES</h2>
<p style="font-size:13px;line-height:1.8">
1. La web está <strong>funcionando al 100%</strong> en cfg-seguros.com <span class="tag-ok">✅</span><br>
2. Deploy automático desde GitHub → Cloudflare Pages <span class="tag-ok">✅</span><br>
3. Las redes están montadas: Instagram, Facebook, LinkedIn, TikTok<br>
4. Los leads llegan por dos vías: formulario Web3Forms + WhatsApp directo<br>
5. Próximo paso importante: <strong>Supervende</strong> (chatbot WhatsApp para capturar datos de clientes)<br>
6. Proyecto aparcado (no tocar): crecimientofinancieroglobal.com<br>
7. Recordatorios activos: saludo 6:30h, publicar redes lun/mié/vie 6:30h, cierre 22:30h<br>
8. Favicon visible en pestaña del navegador desde 18-jul-2026
</p>
</div>

<hr>
<div class="footer">Ficha generada por Alfa · 18 julio 2026 · CFG Seguros</div>

</body>
</html>'''

os.makedirs(OUTDIR, exist_ok=True)
with open(HTML_PATH, "w") as f:
    f.write(html)
print(f"✅ HTML: {HTML_PATH}")

import subprocess
res = subprocess.run([
    "wkhtmltopdf", "--encoding", "UTF-8",
    HTML_PATH, PDF_PATH
], capture_output=True, text=True, timeout=30)
for line in res.stderr.split("\n"):
    if "%" in line or "Done" in line or "error" in line.lower():
        print(f"  {line.strip()}")
print(f"\n✅ PDF final: {PDF_PATH}")
