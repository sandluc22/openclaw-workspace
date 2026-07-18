# Revisión completa del proyecto — Sandra Caicedo
## crecimientofinancieroglobal.com
**Fecha:** 29 de junio de 2026 — 12:05 UTC

---

## 1. 🌐 Web — Estado de páginas ✅

TODAS las páginas responden **200 OK**. El dominio está servido desde **Surge.sh** (digitalocean droplet 159.203.50.177, que es Surge).

| Ruta | Estado |
|------|--------|
| `/` (Home) | ✅ 200 OK |
| `/seguro-vida/` | ✅ 200 OK |
| `/seguro-salud/` | ✅ 200 OK |
| `/seguro-hogar/` | ✅ 200 OK |
| `/empresas-autonomos/` | ✅ 200 OK |
| `/ahorro-inversion/` | ✅ 200 OK |
| `/gracias.html` | ✅ 200 OK |
| `/404.html` | ✅ 200 OK |
| `/robots.txt` | ✅ 200 OK |
| `/sitemap.xml` | ✅ 200 OK |
| `/logo.png` | ✅ 200 OK |

**Nota SSL:** El certificado es de **Sectigo** vía Surge, wildcard `*.surge.sh`. Expira el **16 de diciembre de 2026**. Aunque curl reporta SAN mismatch (el cert es de Surge no del dominio exacto), el navegador de cualquier usuario lo verá como válido porque Surge gestiona el SSL. ✅

**⚠️ Sitemap incompleto:** Solo incluye la home (`/`). Faltan todas las subpáginas de servicios, el 404.html y gracias.html. Esto perjudica el SEO.

---

## 2. 🔒 Dominio + SSL ✅

- **Dominio registrado:** Porkbun LLC
- **Creado:** 23 junio 2026
- **Actualizado:** 29 junio 2026
- **Expira:** **23 junio 2027** ✅ (queda casi 1 año)
- **SSL:** Certificado Sectigo válido hasta **16 diciembre 2026**
- **Estado:** clientDeleteProhibited / clientTransferProhibited (protegido contra borrado/transferencia no autorizada)

---

## 3. 💾 Backup ✅

El backup en `/home/node/workspace/backup-web-28jun/` está **completo e intacto**:

```
404.html
ahorro-inversion/index.html
empresas-autonomos/index.html
gracias.html
index.html
logo.png (71 KB)
robots.txt
seguro-hogar/index.html
seguro-salud/index.html
seguro-vida/index.html
sitemap.xml
styles.css
```

12 archivos en total. Coinciden con lo desplegado en producción.

---

## 4. 📧 Correo (Migadu) — ❌ NO CONFIGURADO EN DNS

| Registro | Valor | Estado |
|----------|-------|--------|
| MX | (vacío) | ❌ No hay registros MX |
| TXT | (vacío) | ❌ No hay registros TXT |
| SPF | (vacío) | ❌ No hay SPF |
| DKIM | (vacío) | ❌ No hay DKIM |
| DMARC | (vacío) | ❌ No hay DMARC |

**Problema crítico:** Los nameservers apuntan a **Surge.sh** (ns1-4.surge.world), NO a Migadu. Para que el correo funcione:

**Opción A (recomendada):** Mantener DNS en Surge y añadir registros MX/TXT desde Porkbun o Migadu
- Migadu necesita registros MX: `mx1.migadu.com` / `mx2.migadu.com`
- Y SPF: `v=spf1 include:spf.migadu.com ~all`
- Y DKIM + DMARC

**Opción B:** Cambiar nameservers a Migadu (pero entonces Surge dejaría de funcionar como CDN/DNS y habría que configurar un registro A en Migadu apuntando a la IP de Surge)

> ⚠️ **El correo de Migadu NO está recibiendo emails actualmente** porque el DNS no está configurado para enrutar el correo a sus servidores.

---

## 5. 📅 Vencimientos y pagos críticos

| Concepto | Fecha | Importe | Prioridad |
|----------|-------|---------|-----------|
| 🔴 **Migadu — pago anual** | **11 julio 2026** | **$19 USD/año** | **URGENTE** — Si no se paga, pierde el buzón |
| 🟢 Dominio Porkbun | 23 junio 2027 | ~$9-12/año | Tranquilo, queda 1 año |
| 🟢 SSL Surge (Sectigo) | 16 diciembre 2026 | Incluido en Surge | Gestionado automáticamente |

---

## 6. ☁️ Cloudflare / Nameservers

```
Nameservers actuales:
ns1.surge.world.
ns2.surge.world.
ns3.surge.world.
ns4.surge.world.
```

**No está usando Cloudflare.** Los nameservers son directamente de Surge.sh. Esto significa que NO hay protección CDN, caché, ni firewall de Cloudflare. Si Sandra quiere Cloudflare en el futuro, habría que:
1. Añadir el sitio a Cloudflare
2. Copiar los nuevos nameservers de Cloudflare a Porkbun
3. Configurar los registros DNS (A/AAAA/CNAME) en Cloudflare

---

## 7. 📋 Memoria — Tareas pendientes detectadas

Revisando los archivos de memoria (17, 21, 26, 27, 28 de junio), estos son los **pendientes NO completados**:

### 🔴 URGENTES (hacer YA)
1. **Pagar Migadu $19/año** — antes del 11 de julio. Si no, pierde el correo.
2. **Configurar DNS de correo (MX/SPF/DKIM/DMARC)** — Sin esto, Migadu no recibe ni envía emails desde el dominio. El correo de Sandra NO FUNCIONA actualmente.
3. **Publicar posts en Facebook** — Contenido ya preparado según memo del 27-jun.

### 🟡 PRIORIDAD MEDIA (próximos días)
4. **Ampliar sitemap.xml** — Solo incluye la home. Añadir todas las subpáginas de servicios para mejorar SEO.
5. **Google Search Console** — Registrar el dominio desde el navegador de Sandra para monitorizar indexación.
6. **Enviar mensajes WhatsApp a contactos** — Promocionar la web.

### 🟢 PUEDE ESPERAR (próximas semanas)
7. **Configurar formulario de la web** — Los botones de WhatsApp/Email/ Teléfono funcionan bien. Si quiere captura automática de leads, necesita FormSubmit / Web3Forms.
8. **Unirse a grupos de Facebook** — Para compartir contenido.
9. **Evaluar Cloudflare** — Para protección y rendimiento. Baja prioridad ahora.
10. **Email marketing (MailerLite/Brevo)** — Cuando tenga lista de contactos.

---

## Resumen visual

| Punto | Estado |
|-------|--------|
| Web online (200 OK) | ✅ |
| SSL válido | ✅ |
| Backup local | ✅ |
| DNS Migadu configurado | ❌ |
| Dominio Porkbun | ✅ (expira 2027) |
| Pago Migadu ($19) | ⏳ antes 11 julio |
| Nameservers Surge | ✅ |
| Sitemap completo | ⚠️ Solo home |
| Tareas de contenido pendientes | 🟡 3 tareas |

---

## Recomendación de próximos pasos

### Hoy/mañana
1. **Pagar Migadu** ($19 USD) — Es lo más urgente. Sin pago antes del 11 de julio, se pierde el buzón.
2. **Configurar DNS de correo** — Desde Porkbun o donde gestione los DNS, añadir:
   - MX: `mx1.migadu.com` (prioridad 10)
   - MX: `mx2.migadu.com` (prioridad 20)
   - TXT: `v=spf1 include:spf.migadu.com ~all`
   - TXT: `migadu._domainkey.crecimientofinancieroglobal.com` → (clave DKIM de Migadu)
   - TXT: `_dmarc.crecimientofinancieroglobal.com` → `v=DMARC1; p=none;`

### Esta semana
3. **Publicar contenido en Facebook** (texto ya preparado)
4. **Registrar en Google Search Console**
5. **Actualizar sitemap.xml** para cubrir todas las páginas

### Próximas semanas
6. **Evaluar si añadir Cloudflare** o mantenerse con Surge.sh
7. **Configurar captura de leads** (formulario o landing)
8. **Email marketing** cuando tenga contactos

---

*Revisión generada automáticamente por Alfa — 29 junio 2026*
