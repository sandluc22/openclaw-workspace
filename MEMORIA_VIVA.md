# MEMORIA VIVA - Estado de Proyectos

Última actualización: **Lunes 13 Julio 2026**

---

## 🔵 CFG — Crecimiento Financiero Global
**Última sesión:** 13 julio 2026

### Estado actual
- Web en Netlify, servida vía Cloudflare (proxy naranja activo)
- Diseño intacto (azul/oscuro)
- ❌ **Formulario no envía** — apunta a `lhr.life` (caído)
- Worker `yellow-bar-eceb` activo en Cloudflare con diseño y formulario funcionando

### Bloqueos
- Netlify: los deploys por API se suben pero no se publican como activos
- Para actualizar: Sandra debe arrastrar index.html desde Netlify > deploys
- Token Netlify actual: nfp_hLB6E83aw1y2sLiHNP8gR9Fg2iT7hyKd676a (solo acceso a CFG, no a Club Contable)

### Pendiente
- Subir HTML con Web3Forms a Netlify (desde PC de Sandra)

---

## 🟡 Club Contable
**Última sesión:** 13 julio 2026

### Estado actual
- ✅ HTML completo (77KB) con login, categorías, diseño — guardado en `/home/node/workspace/clubcontable/codigo/index.html`
- ❌ Sin servidor activo
- DNS apunta a Netlify (nsone.net) pero Netlify no tiene contenido
- Token Netlify no tiene acceso al site de CC

### Bloqueos
- Dominio registrado en Namecheap (email: crecimientofinancieroglobal@gmail.com)
- Necesito claves Namecheap para cambiar nameservers

### Pendiente
- Decidir hosting: Cloudflare Worker, Railway, otro
- Cambiar DNS

---

## 🟢 cfgseguros.com
- En fase de decisión
- Opciones: dominio nuevo (~12€/año), subdominio (gratis), integrar en web actual
- Correo gratuito con Migadu

---

## 🟣 Gafi
- Marketing de afiliados
- Sin empezar

---

## 🟠 Gestión de taller
- Sandra lo mencionó, sin detalles
- Pendiente preguntar: tipo de taller, qué necesita

---

## 📧 Migadu
- ✅ info@crecimientofinancieroglobal.com funcionando
- 💡 Se pueden añadir más dominios gratis

---

## 🔐 Contraseñas
- Todo en `/home/node/workspace/CONTRASEÑAS/`
- Tokens Cloudflare en cloudflare.md
- Correo CFG: crecimientofinancieroglobal@gmail.com
- Netlify email: crecimientofinancieroglobal@gmail.com (login con Google)

---

## ⏭️ Próximos pasos (Martes 14 Jul)
1. Decidir hosting para Club Contable + claves Namecheap
2. Formulario CFG
3. Decidir cfgseguros.com
4. Preguntar detalles del taller
