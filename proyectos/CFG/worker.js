export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Redirigir www a dominio sin www
    if (url.hostname.startsWith('www.')) {
      url.hostname = url.hostname.slice(4);
      return Response.redirect(url.toString(), 301);
    }

    // Servir logo.png
    if (url.pathname === '/logo.png') {
      const response = await fetch('https://raw.githubusercontent.com/sandluc22/clubcontable/main/cfg/logo.png');
      return new Response(response.body, {
        headers: {
          'content-type': 'image/png',
          'cache-control': 'public, max-age=86400'
        }
      });
    }

    // HTML principal
    const html = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.5, user-scalable=yes" />
  <title>Crecimiento Financiero Global</title>
  <meta name="description" content="Encuentra el seguro perfecto para ti y tu familia con Crecimiento Financiero Global. Asesoría personalizada, comparamos las mejores aseguradoras." />
  <meta property="og:title" content="Crecimiento Financiero Global — Tu seguro, tu tranquilidad" />
  <meta property="og:description" content="Compara y elige el seguro ideal con asesoría personalizada. Sin compromiso." />
  <meta property="og:url" content="https://crecimientofinancieroglobal.com" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://crecimientofinancieroglobal.com/logo.png" />
  <meta property="og:locale" content="es_ES" />
  <link rel="canonical" href="https://crecimientofinancieroglobal.com" />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💰</text></svg>" />
  <style>
    :root {
      --naranja: #f97316;
      --naranja-oscuro: #ea580c;
      --naranja-claro: #fed7aa;
      --blanco: #ffffff;
      --gris-claro: #f9fafb;
      --gris: #6b7280;
      --gris-oscuro: #1f2937;
      --negro: #111827;
      --sombra: 0 4px 24px rgba(0,0,0,0.08);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      background: var(--gris-claro);
      color: var(--negro);
      line-height: 1.6;
      scroll-behavior: smooth;
    }
    .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
    header {
      background: linear-gradient(135deg, var(--naranja), var(--naranja-oscuro));
      color: var(--blanco);
      padding: 20px 0;
      position: sticky; top: 0; z-index: 100;
      box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    }
    header .container { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; }
    .logo { display: flex; align-items: center; gap: 12px; }
    .logo img { height: 48px; width: auto; border-radius: 8px; }
    .logo h1 { font-size: 1.3rem; font-weight: 700; line-height: 1.2; }
    nav { display: flex; gap: 8px; flex-wrap: wrap; }
    nav a { color: var(--blanco); text-decoration: none; padding: 8px 14px; border-radius: 8px; font-weight: 500; font-size: 0.9rem; transition: background 0.2s; }
    nav a:hover { background: rgba(255,255,255,0.2); }
    .hero {
      background: linear-gradient(135deg, var(--naranja), var(--naranja-oscuro));
      color: var(--blanco); padding: 80px 0; text-align: center;
    }
    .hero h2 { font-size: 2.5rem; font-weight: 800; margin-bottom: 20px; line-height: 1.2; }
    .hero p { font-size: 1.2rem; max-width: 700px; margin: 0 auto 30px; opacity: 0.95; }
    .hero .btn {
      background: var(--blanco); color: var(--naranja);
      padding: 16px 40px; border-radius: 50px;
      font-size: 1.1rem; font-weight: 700; text-decoration: none; display: inline-block;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .hero .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.2); }
    section { padding: 60px 0; }
    section:nth-child(even) { background: var(--blanco); }
    .section-title { font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px; color: var(--negro); }
    .section-title span { color: var(--naranja); }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; }
    .card {
      background: var(--blanco); border-radius: 16px; padding: 32px 24px;
      box-shadow: var(--sombra); text-align: center; transition: transform 0.2s;
    }
    .card:hover { transform: translateY(-4px); }
    .card .icon { font-size: 2.5rem; margin-bottom: 16px; }
    .card h3 { font-size: 1.2rem; margin-bottom: 10px; color: var(--negro); }
    .card p { color: var(--gris); font-size: 0.95rem; }
    .form-section { background: linear-gradient(135deg, var(--naranja-claro), var(--gris-claro)); }
    form {
      max-width: 560px; margin: 0 auto;
      background: var(--blanco); padding: 40px 32px;
      border-radius: 20px; box-shadow: var(--sombra);
    }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; font-weight: 600; margin-bottom: 6px; color: var(--negro); font-size: 0.95rem; }
    .form-group input, .form-group select {
      width: 100%; padding: 14px 16px; border: 2px solid #e5e7eb;
      border-radius: 12px; font-size: 1rem; transition: border-color 0.2s; background: var(--gris-claro);
    }
    .form-group input:focus, .form-group select:focus { outline: none; border-color: var(--naranja); }
    form button {
      width: 100%; background: linear-gradient(135deg, var(--naranja), var(--naranja-oscuro));
      color: var(--blanco); border: none; padding: 16px; border-radius: 12px;
      font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s;
    }
    form button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(249,115,22,0.3); }
    form button:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }
    .form-ok { background: #dcfce7; color: #166534; padding: 14px 20px; border-radius: 12px; text-align: center; font-weight: 600; margin-top: 16px; display: none; }
    footer { background: var(--gris-oscuro); color: var(--blanco); text-align: center; padding: 30px 0; font-size: 0.9rem; }
    footer a { color: var(--naranja-claro); text-decoration: none; }
    @media (max-width: 768px) {
      header .container { flex-direction: column; text-align: center; }
      .logo { justify-content: center; }
      .hero h2 { font-size: 1.8rem; }
      .hero p { font-size: 1rem; }
      section { padding: 40px 0; }
      form { padding: 24px 16px; }
    }
  </style>
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <img src="/logo.png" alt="Crecimiento Financiero Global" />
        <h1>Crecimiento<br />Financiero Global</h1>
      </div>
      <nav>
        <a href="#servicios">Servicios</a>
        <a href="#seguros">Seguros</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="container">
      <h2>Tu tranquilidad empieza aquí</h2>
      <p>Te ayudamos a encontrar el seguro perfecto para ti y tu familia. Asesoría personalizada, sin compromiso.</p>
      <a href="#contacto" class="btn">Solicitar información</a>
    </div>
  </section>

  <section id="servicios">
    <div class="container">
      <h2 class="section-title">¿Por qué <span>elegirnos?</span></h2>
      <div class="cards">
        <div class="card"><div class="icon">🛡️</div><h3>Asesoría personalizada</h3><p>Te escuchamos, analizamos tus necesidades y te recomendamos la mejor opción.</p></div>
        <div class="card"><div class="icon">📊</div><h3>Comparamos por ti</h3><p>Trabajamos con las mejores aseguradoras del mercado para ofrecerte el mejor precio.</p></div>
        <div class="card"><div class="icon">⏱️</div><h3>Respuesta rápida</h3><p>Te respondemos en menos de 24 horas. Sin esperas ni papeleos.</p></div>
      </div>
    </div>
  </section>

  <section id="seguros">
    <div class="container">
      <h2 class="section-title">Tipos de <span>seguro</span></h2>
      <div class="cards">
        <div class="card"><div class="icon">🏥</div><h3>Seguro de Salud</h3><p>Cobertura médica completa, consultas, hospitalización y más.</p></div>
        <div class="card"><div class="icon">🚗</div><h3>Seguro de Auto</h3><p>Protege tu vehículo con la mejor cobertura al mejor precio.</p></div>
        <div class="card"><div class="icon">🏠</div><h3>Seguro de Hogar</h3><p>Tu casa protegida ante cualquier imprevisto.</p></div>
        <div class="card"><div class="icon">👨‍👩‍👧‍👦</div><h3>Seguro de Vida</h3><p>Garantiza el futuro de los tuyos con un plan a tu medida.</p></div>
        <div class="card"><div class="icon">💼</div><h3>Seguro Empresarial</h3><p>Protege tu negocio con coberturas adaptadas a tu actividad.</p></div>
        <div class="card"><div class="icon">✈️</div><h3>Seguro de Viaje</h3><p>Viaja tranquilo con asistencia en viaje las 24 horas.</p></div>
      </div>
    </div>
  </section>

  <section class="form-section" id="contacto">
    <div class="container">
      <h2 class="section-title">Solicita tu <span>asesoría</span></h2>
      <form id="contactForm">
        <input type="hidden" name="access_key" value="7d8a5f44-2eae-4a17-8581-6e8e29723d9e" />
        <div class="form-group">
          <label>Nombre</label>
          <input type="text" name="nombre" required placeholder="Tu nombre" />
        </div>
        <div class="form-group">
          <label>Teléfono</label>
          <input type="tel" name="telefono" required placeholder="Tu teléfono" />
        </div>
        <div class="form-group">
          <label>Correo electrónico</label>
          <input type="email" name="email" required placeholder="Tu correo" />
        </div>
        <div class="form-group">
          <label>Fecha de nacimiento</label>
          <input type="date" name="fecha_nacimiento" required />
        </div>
        <div class="form-group">
          <label>Tipo de seguro que buscas</label>
          <select name="seguro" required>
            <option value="">Selecciona una opción</option>
            <option>Salud</option><option>Auto</option><option>Hogar</option><option>Vida</option><option>Empresarial</option><option>Viaje</option><option>No lo sé todavía</option>
          </select>
        </div>
        <div class="form-group">
          <label>Aseguradora de interés</label>
          <select name="aseguradora_interes" required>
            <option value="">Selecciona una opción</option>
            <option>Sanitas</option><option>Adeslas</option><option>Asisa</option><option>Mapfre</option><option>DKV</option><option>AXA</option><option>Allianz</option><option>Generali</option><option>Caser</option><option>Reale</option><option>Aegon</option><option>Otra</option><option>No lo sé todavía</option>
          </select>
        </div>
        <button type="submit">Enviar solicitud</button>
      </form>
      <div id="formOk" class="form-ok">✅ Mensaje enviado. Te responderemos en menos de 24h.</div>
    </div>
  </section>

  <footer>
    <div class="container">
      <p>&copy; 2026 Crecimiento Financiero Global — Todos los derechos reservados</p>
      <p><a href="mailto:info@crecimientofinancieroglobal.com">info@crecimientofinancieroglobal.com</a></p>
    </div>
  </footer>

  <script>
  document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = this.querySelector('button[type="submit"]');
    const original = btn.textContent;
    btn.textContent = '⏳ Enviando...';
    btn.disabled = true;
    try {
      const formData = new FormData(this);
      const data = {};
      formData.forEach((val, key) => data[key] = val);
      data.access_key = '7d8a5f44-2eae-4a17-8581-6e8e29723d9e';

      const w3res = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      const w3result = await w3res.json();

      const token = '810902…PFzA';
      const chatId = '7890204626';
      let mensaje = '';
      mensaje += '\\u{1F514} *Nuevo lead CFG Seguros*\\n\\n';
      mensaje += '\\u{1F464} *Nombre:* ' + data.nombre + '\\n';
      mensaje += '\\u{1F4DE} *Tel\\u00E9fono:* ' + data.telefono + '\\n';
      mensaje += '\\u2709\\uFE0F *Correo:* ' + data.email + '\\n';
      mensaje += '\\u{1F382} *Fecha nac.:* ' + data.fecha_nacimiento + '\\n';
      mensaje += '\\u{1F4CB} *Seguro:* ' + data.seguro + '\\n';
      mensaje += '\\u{1F3E2} *Aseguradora:* ' + data.aseguradora_interes + '\\n';
      mensaje += '\\u{1F4C5} *Fecha:* ' + new Date().toLocaleDateString('es-ES');

      const url = 'https://api.telegram.org/bot' + token + '/sendMessage';
      const body = JSON.stringify({ chat_id: chatId, text: mensaje, parse_mode: 'Markdown' });
      const resTelegram = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body });
      const telegramResult = await resTelegram.json();

      if (telegramResult.ok && w3result.success) {
        this.reset();
        document.getElementById('formOk').style.display = 'block';
        setTimeout(() => document.getElementById('formOk').style.display = 'none', 5000);
      } else {
        alert('Error al enviar. Int\\u00E9ntalo de nuevo.');
      }
    } catch(err) {
      alert('Error de conexi\\u00F3n. Int\\u00E9ntalo de nuevo.');
    } finally {
      btn.textContent = original;
      btn.disabled = false;
    }
  });
  </script>
</body>
</html>`;

    return new Response(html, {
      headers: {
        'content-type': 'text/html; charset=utf-8',
        'cache-control': 'public, max-age=0, s-maxage=300'
      }
    });
  }
};
