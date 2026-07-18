#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server, urllib.parse, subprocess, smtplib
from email.mime.text import MIMEText

HOST = '0.0.0.0'
PORT = 18888

class FormHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode()
        data = urllib.parse.parse_qs(body)
        
        flat = {k: v[0] if isinstance(v, list) else v for k, v in data.items()}
        nombre = flat.get('nombre', 'No indicado')
        contacto = flat.get('contacto', 'No indicado')
        fecha_nac = flat.get('fecha_nacimiento', 'No indicado')
        interes = flat.get('interes', 'No indicado')
        mensaje = flat.get('mensaje', 'No indicado')
        pagina = flat.get('pagina', 'Web')
        
        email_body = f"""Nuevo contacto desde la web - CFG

Nombre: {nombre}
Contacto: {contacto}
Fecha nacimiento: {fecha_nac}
Interes: {interes}
Mensaje: {mensaje}
Pagina: {pagina}
"""
        
        try:
            msg = MIMEText(email_body, 'plain', 'utf-8')
            msg['Subject'] = f'[CFG] Contacto web: {nombre}'
            msg['From'] = 'info@crecimientofinancieroglobal.com'
            msg['To'] = 'crecimientofinancieroglobal@gmail.com'
            
            s = smtplib.SMTP('smtp.migadu.com', 587, timeout=15)
            s.starttls()
            s.login('info@crecimientofinancieroglobal.com', 'AlfaySandra!')
            s.send_message(msg)
            s.quit()
            print(f'OK: {nombre}')
        except Exception as e:
            print(f'SMTP error: {e}')
            try:
                p = subprocess.run(['msmtp', '-a', 'cfg', 'crecimientofinancieroglobal@gmail.com'], 
                    input=email_body.encode(), capture_output=True, timeout=10)
                print(f'msmtp: {p.returncode}')
            except Exception as e2:
                print(f'msmtp fail: {e2}')
        
        self.send_response(302)
        self.send_header('Location', 'https://crecimientofinancieroglobal.com/gracias.html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

server = http.server.HTTPServer((HOST, PORT), FormHandler)
print(f'Form server v2 ready on port {PORT}')
server.serve_forever()
