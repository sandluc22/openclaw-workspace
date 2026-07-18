const http = require('http');
const fs = require('fs');
const { exec } = require('child_process');

const PORT = process.env.FORM_PORT || 18888;

function sendEmail(formData) {
  return new Promise((resolve, reject) => {
    const nombre = formData.nombre || 'No especificado';
    const contacto = formData.contacto || 'No especificado';
    const fecha_nacimiento = formData.fecha_nacimiento || 'No especificada';
    const interes = formData.interes || 'No especificado';
    const mensaje = formData.mensaje || '';
    const pagina = formData.pagina || 'Página principal';

    const email = `Subject: 📩 Nuevo contacto: ${interes}
From: Crecimiento Financiero Global <info@crecimientofinancieroglobal.com>
To: crecimientofinancieroglobal@gmail.com
Content-Type: text/plain; charset=UTF-8

👤 Nombre: ${nombre}
🎂 Fecha nacimiento: ${fecha_nacimiento}
📞 Contacto: ${contacto}
🔍 Interés: ${interes}
📍 Página: ${pagina}

💬 Mensaje:
${mensaje || 'No escribió mensaje adicional.'}
`;

    const child = exec('msmtp crecimientofinancieroglobal@gmail.com', (err) => {
      if (err) reject(err);
      else resolve();
    });
    child.stdin.write(email);
    child.stdin.end();
  });
}

const server = http.createServer(async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      try {
        const params = new URLSearchParams(body);
        const formData = Object.fromEntries(params);
        
        await sendEmail(formData);
        console.log(`✅ Enviado: ${formData.nombre} - ${formData.interes}`);
        
        res.writeHead(302, { 'Location': 'https://crecimientofinancieroglobal.com/gracias.html' });
        res.end();
      } catch (e) {
        console.error('Error:', e.message);
        res.writeHead(302, { 'Location': 'https://crecimientofinancieroglobal.com/gracias.html' });
        res.end();
      }
    });
    return;
  }

  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('OK');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Form server ready on port ${PORT}`);
  fs.writeFileSync('/tmp/form_server_pid.txt', String(process.pid));
});

// Keep alive
process.on('SIGINT', () => process.exit());
setInterval(() => {}, 60000);
