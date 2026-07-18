# 📋 TAREAS PENDIENTES — ÍNDICE

**Las tareas se guardan por fecha en archivos separados.**

---

## 📂 Archivos por fecha

- [12-jul-2026](./2026-07-12.md) — CFG formulario, Fiverr, Hotmart, Club Contable

---

## 📌 Histórico de sesiones

_(Se añade cada día que trabajemos)_

### ✅ COMPLETADO
- ✅ **SSL resuelto** — Cloudflare proxy naranja, Google Trust, válido hasta 25-sep-2026
- ✅ **DNS** — A record `@` → Netlify con proxy naranja. Web responde 200 OK
- ✅ **Formulario** — Quitado campo Edad. Añadidos: **Fecha de nacimiento** + **Aseguradora de interés**
- ✅ **Desplegable aseguradoras:** Sanitas, Adeslas, Asisa, Mapfre, DKV, AXA, Allianz, Generali, Caser, Reale, Aegon, Otra, No lo sé todavía
- ✅ **"¿Qué seguro quieres?" repetido** — corregido (solo uno)
- ✅ **Color** — Cambiado de amarillo (#f0c040) a **naranja** (#f97316)
- ✅ **Logo.png** — Sin amarillo, compatible con naranja
- ✅ **`form.php`** — Configurado para enviar a info@crecimientofinancieroglobal.com
- ✅ **Sitemap** — Actualizado: **15 URLs** con lastmod, changefreq, priority
- ✅ **Robots.txt** — Permite Googlebot, bloquea IA, apunta sitemap
- ✅ **SEO básico** — Title, meta description, OG tags, canonical
- ✅ **Netlify token renovado** por Sandra (último: nfp_YEHGmHDD38cdGz3ivUFC6o9obMxa4uZE29e0) — expira 16-jul
- ✅ **Último deploy manual desde ordenador de Sandra** — 10:54 PM, index.html 15.7 KB

### ❌ POR VERIFICAR (10-jul)
- [ ] **Abrir https://crecimientofinancieroglobal.com** — ¿se ve naranja o amarilla?
- [ ] Si amarilla: **purga de caché en Cloudflare** (ya se hizo 3 veces, puede tardar)
- [ ] Si aún así no: **quitar proxy naranja temporalmente** en DNS de Cloudflare
- [ ] Verificar que el `form.php` + `sitemap.xml` están en el deploy (subí yo desde CLI pero falló)

### 📌 PRÓXIMOS
- [ ] **Google Search Console** — Verificar dominio con crecimientofinancieroglobal@gmail.com
- [ ] Enviar sitemap.xml a Google para indexación
- [ ] Probar que el formulario envía datos a info@

### 🆕 MAÑANA 13-JUL: FORMULARIO CFG
- [ ] **Formspree** — Sandra se registra en formspree.io y pasa la URL
- [ ] Alfa conecta el formulario a la web y despliega

### 🆕 FIVERR: SEGUNDO GIG (Asistente Virtual + Contable + Traducciones)
- [ ] Definir título, descripción y paquetes
- [ ] Incluir: contabilidad, facturación, gestión documental, **traducción de textos**
- [ ] Crear el Gig en Fiverr (sin publicar aún)

### 🆕 CLUB CONTABLE PENDIENTE EXTRA
- [ ] **Suscripciones** — Crear plan de venta por suscripción (precio, funcionalidades, cómo se cobra)
- [ ] Definir qué incluye cada plan (usuarios, tareas, informes...)

---

## 🟢 Club Contable — Backend en Railway

**Estado:** ❌ Servicio caído. Railway lo eliminó tras "Application failed to respond".

- [ ] **Cuando Sandra tenga tiempo:** Entrar a https://railway.app
- [ ] Proyecto **clubcontable**
- [ ] **"+ New Service"** → **"Deploy from GitHub repo"** → sandluc22/clubcontable
- [ ] Esperar build y pasar la URL a Alfa

---

## 🔵 Club Contable — Frontend
- [ ] Actualizar frontend en Surge con la URL del backend en Railway (cuando funcione)

---

## 🟣 Producto SaaS
- [ ] Definir modelo de negocio y precios
- [ ] Crear landing page
- [ ] Probar con primeros clientes

---

## 🔐 Referencia de claves

| Servicio | Usuario | Clave/Acceso |
|---|---|---|
| **GitHub** | sandluc22 | AlfaySandra.1 |
| **Cloudflare CFG** | crecimientofinancieroglobal@gmail.com | AlfaySandra.1 |
| **Netlify CFG** | crecimientofinancieroglobal@gmail.com | Último token: nfp_YEHGmHDD38cdGz3ivUFC6o9obMxa4uZE29e0 (exp: 16-jul) |
| **Migadu CFG** | crecimientofinancieroglobal@gmail.com | AlfaySandra.1 |
| **Surge CFG** | sandluc22@gmail.com | AlfaySandra.1 |
| **Gmail Club Contable** | admin.clubcontable@gmail.com | AlfaySandra. |
| **Railway** | Via GitHub (sandluc22) | Misma que GitHub |
| **Railway Project ID** | `0c27117d-0be1-476e-92ba-1b836c2ce477` | — |
| **Railway Service ID** | `7334b3ae-e5ad-450c-9381-355ccb74e9f4` | — |
| **LinkedIn** | sandluc22@gmail.com (contraseña no guardada) | — |

---

> **📌 Resumen:** Ayer (09-jul) se trabajó mucho: cambios de color a naranja, formulario con Fecha de nacimiento + desplegable de aseguradoras, sitemap mejorado. Se subió el index.html a Netlify manualmente pero Cloudflare no actualiza la caché. Pendiente de verificar hoy. Si aún no se ve, poner DNS en gris (solo) y volver a naranja.

*Última revisión: 09-jul-2026 23:02h*
