# 📋 TABLERO - SEGUIMIENTO DE TAREAS
*Actualizado: 11 julio 2026 — 21:50*

---

## 🔶 CFG - Crecimiento Financiero Global / CFG Seguros

### ✅ COMPLETADO

#### Diseño web y hosting
- [x] Index.html modificado (naranja, formulario, captcha, fecha nacimiento)
- [x] Page Rule creada en Cloudflare
- [x] Worker `yellow-bar-eceb` creado con código naranja subido
- [x] Tokens Cloudflare: workers-alfa, Rules CFG, alfa (3 nuevos)
- [x] Google Search Console: dominio verificado y sitemap enviado
- [x] SSL funcionando
- [x] Analitycs instalados
- [x] Porkbun DNS verificado
- [x] Carpeta CONTRASEÑAS/ creada (14 archivos)
- [x] Worker con HTML versión naranja (fecha nacimiento + aseguradora deseada)
- [x] Route Workers eliminada (dominio vuelve a Netlify)
- [x] Page Rule eliminada (dominio vuelve a Netlify)
- [x] HTML final generado: `/home/node/workspace/index-final.html`
- [x] HTML con Netlify Forms: `/tmp/index-netlify.html`
- [x] Deploy Netlify Drop con index.html 3.7KB (incompleto)
- [x] Deploy Netlify Drop 14.9KB (HTML sin netlify en form)

#### Formulario
- [x] **Google Forms creado** con todos los campos (nombre, email, teléfono, fecha nacimiento, aseguradora, tipo seguro, comentarios)
- [x] Google Forms conectado a hoja de cálculo
- [x] Cloudflare Pages creado: proyecto `cfg-web` (URL: cfg-web-5jw.pages.dev)
- [x] Deploy en CF Pages con botón a Google Forms
- [x] Hyperlink redirect URL to Google Forms
- [x] Netlify completado: crecimientofinancieroglobal.com cargando web sin formulario

#### Redes Sociales CFG Seguros
- [x] **Instagram** (@cfg.seguros): primer post de lanzamiento publicado ✅
- [x] **Facebook** (CFG Seguros): primer post de lanzamiento publicado ✅
- [x] **WhatsApp**: mensajes enviados a contactos con el texto de presentación
- [x] **7 imágenes definitivas** para redes (formato post completo, sin texto extra)
- [x] **Diseño visual definitivo**: color #143278 (Azul CFG), tarjeta #284b9b, acento #fbbf24, Liberation Sans Bold
- [x] **Calendario de publicaciones** creado y guardado en `proyectos/CFG/redes/CALENDARIO.md`
- [x] **Textos por red social** guardados con correo (sin formulario):
  - Instagram (7 posts) → `redes/instagram/POSTS.md`
  - Facebook (5 posts) → `redes/facebook/POSTS.md`
  - LinkedIn (4 posts) → `redes/linkedin/POSTS.md`
  - WhatsApp (6 plantillas) → `redes/whatsapp/MENSAJES.md`
- [x] **Google My Business**: ficha creada para CFG Seguros (zona servicio Madrid, pendiente carta verificación)

#### Club Contable
- [x] Login con 4 usuarios creado (Sandra, María Ángel, Yurleny, Kareling)
- [x] 6 categorías principales con subcategorías
- [x] Tareas recategorizadas: IVA/Retefuente/Renta → Impuestos, Seguridad Social → Laboral
- [x] Nameservers cambiados en Namecheap a Netlify para clubcontable.com
- [x] HTML guardado en: `/home/node/workspace/clubcontable/codigo/index.html`

---

## ⏳ EN PROGRESO / PENDIENTE

### [ ] MAÑANA (12 julio)

#### PRIORIDAD 1: Formulario CFG
- [ ] Terminar formulario funcional (montar en Cloudflare Pages y apuntar dominio crecimientofinancieroglobal.com)
- [ ] Que envíe datos reales a Google Sheets

#### Redes Sociales
- [ ] Publicar Seguro de Hogar 🏠 (lunes 13) en Instagram + Facebook
- [ ] LinkedIn: publicar página de empresa y primer post profesional
- [ ] Google My Business: esperar carta de verificación (1-2 semanas)

#### Club Contable
- [ ] Esperar propagación DNS (puede tardar hasta 24h)
- [ ] Confirmar que Netlify emite SSL automático
- [ ] Verificar que `clubcontable.com` carga con login y subcategorías
- [ ] Añadir más tareas a las subcategorías nuevas

---

## 🛑 BLOQUEADO

- **Club Contable**: Web no carga porque DNS del dominio apuntaban a Porkbun — YA CAMBIADOS a Netlify, pendiente propagación
- **Club Contable**: HTML actual usa localStorage (sin backend) — pendiente migración futura a backend con BD
- **Google My Business CFG**: Pendiente carta de verificación postal (1-2 semanas a Av. Jaca 14, 28022 Madrid)

---

## 🎯 OBJETIVOS FUTUROS (visibles siempre)

### 💰 Club Contable
> Vender como **servicio por suscripción mensual** a contadores, asesores y pequeños negocios. Cada contador con su panel de clientes, ingresos recurrentes.

### 🚀 Fivver
> Personalizar perfil, crear gigs de contabilidad/asesoría, enviar presupuestos y empezar a facturar rápido.

---

## 📁 ESTRUCTURA DE ARCHIVOS

### CFG Seguros
```
proyectos/CFG/
├── credenciales-redes.md     ← Todo el diseño visual + datos
├── redes/
│   ├── CALENDARIO.md         ← Calendario de publicaciones
│   ├── instagram/POSTS.md    ← 7 posts para Instagram
│   ├── facebook/POSTS.md     ← 5 posts para Facebook
│   ├── linkedin/POSTS.md     ← 4 posts para LinkedIn
│   └── whatsapp/MENSAJES.md  ← 6 plantillas WhatsApp
```

### Club Contable
```
clubcontable/codigo/
├── index.html                ← Web con login + 6 categorías + subcategorías
├── index.html.bak            ← Backup original
├── index.html.bak2           ← Backup con login
└── index.html.bak_antes_categorias  ← Backup antes de categorías
```

### Contraseñas y credenciales
```
CONTRASEÑAS/
├── cloudflare.md
├── netlify.md
└── ...
```

---

*Próxima actualización: 12 julio 2026*
