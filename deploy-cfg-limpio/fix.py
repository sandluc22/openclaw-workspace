import re

with open('index.html') as f:
    c = f.read()

# 1. TITLE
c = c.replace(
    '<title>Crecimiento Financiero Global · colaboradores de Grupo Galilea</title>',
    '<title>CFG Seguros · Protege lo que importa</title>'
)

# 2. LOGO - incrustar SVG
c = re.sub(
    r'<img[^>]*logo\.png[^>]*>',
    '<div style="display:inline-block;vertical-align:middle;width:100px;height:105px;margin-right:8px"><svg viewBox="0 0 200 55" width="100%" height="100%"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#0a1f44"/><stop offset="100%" style="stop-color:#1a3a7a"/></linearGradient></defs><path d="M10 5 L40 5 L47 16 L40 28 L25 39 L10 28 L3 16 Z" fill="url(#g)"/><polyline points="16 19 23 27 34 13" fill="none" stroke="#f0c040" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><text x="56" y="30" font-family="Arial,sans-serif" font-size="30" font-weight="800" fill="#0a1f44">CFG</text><text x="56" y="48" font-family="Arial,sans-serif" font-size="16" font-weight="600" fill="#f0c040" letter-spacing="3.5">SEGUROS</text></svg></div>',
    c
)

# 3. FORM - quitar netlify
c = c.replace(
    '<form name="seguros-cfg" id="contactForm" netlify>',
    '<form name="seguros-cfg" id="contactForm">'
)

# 4. FORM - añadir access_key oculto antes del boton
c = c.replace(
    '<button type="submit" class="btn">📨 Enviar consulta</button>',
    '<input type="hidden" name="access_key" value="7d8a5f44-6c4c-423e-be9f-6ac9b13d7d41">\n          <input type="hidden" name="subject" value="Nuevo lead CFG Seguros">\n          <button type="submit" class="btn">📨 Enviar consulta</button>'
)

# 5. SCRIPT - reemplazar completamente
script_match = re.search(r'<script>\n// Envío del formulario[\s\S]*?</script>', c)
if script_match:
    old_script = script_match.group()
    print(f"Script anterior: {len(old_script)} chars")
else:
    print("Script no encontrado!")
    old_script = "NO_ENCONTRADO"

new_script = '''<script>
// Envío del formulario a Web3Forms
document.getElementById('contactForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const btn = this.querySelector('.btn');
  const orig = btn.textContent;
  btn.textContent = 'Enviando...';
  btn.disabled = true;

  const formData = new FormData(this);
  const data = {};
  formData.forEach((v, k) => data[k] = v);
  data.access_key = '7d8a5f44-6c4c-423e-be9f-6ac9b13d7d41';
  data.subject = 'Nuevo lead CFG Seguros · cfg-seguros.com';

  let ok = false;
  try {
    const r = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    const j = await r.json();
    ok = j.success;
  } catch(e) { console.log('W3 error:', e); }

  // Telegram tambien
  try {
    const t = '7667281000:AAH_RQFbr-2rG04vm5bGoQASG8xHqRqPFzA';
    const msg = '*Nuevo lead · CFG Seguros*\\n'
      + '*Nombre:* ' + (data.nombre || '-') + '\\n'
      + '*Telefono:* ' + (data.telefono || '-') + '\\n'
      + '*Email:* ' + (data.email || '-') + '\\n'
      + '*Seguro:* ' + (data.seguro || '-') + '\\n'
      + '*Mensaje:* ' + (data.message || '-');
    await fetch('https://api.telegram.org/bot' + t + '/sendMessage', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: '7890204626', text: msg, parse_mode: 'Markdown' })
    });
  } catch(e2) { console.log('TG error:', e2); }

  btn.textContent = orig;
  btn.disabled = false;

  if (ok) {
    this.reset();
    document.getElementById('formOk').style.display = 'block';
    setTimeout(() => document.getElementById('formOk').style.display = 'none', 6000);
  } else {
    alert('Error al enviar. Escríbenos a info@cfg-seguros.com');
  }
});
</script>'''

c = c.replace(old_script, new_script)

with open('index_final.html', 'w') as f:
    f.write(c)

print(f"Guardado: {len(c)} bytes")
print(f"Titulo CFG: {'CFG Seguros' in c}")
print(f"Logo grande: {'width:100px' in c}")
print(f"access_key: {'7d8a5f44' in c}")
print(f"Web3Forms: {'api.web3forms.com' in c}")
print(f"Telegram: {'7667281000' in c}")
print(f"No netlify: {'netlify' not in c}")
print(f"addEventListener: {'addEventListener' in c}")
print(f"formOk: {'formOk' in c}")
