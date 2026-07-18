# MEMORY.md — Memoria permanente de Sandra

> Esta es tu memoria permanente y el ÚNICO archivo de memoria que se carga solo en cada sesión. Mantenla SIEMPRE al día. Aquí está el mapa de TODO tu trabajo; los detalles viven en las carpetas y en tu diario `memory/AAAA-MM-DD.md`.

## Quién es Sandra
Sandra Caicedo — agente de **Grupo Galilea** (seguros, ahorro e inversión) en Madrid, opera en toda España. Vendió su primera póliza y está montando su presencia online desde cero; dispone de ~2h/semana. También lleva **Club Contable** (Colombia). Tú eres **Alfa**, su asistente autónomo.

## Mapa de tu espacio de trabajo (/home/node/workspace)
Cuando trabajes en algo, ENTRA a la carpeta correspondiente y revisa/actualiza sus archivos. Todo esto ya existe:

**Seguros — CFG / Grupo Galilea (lo principal):**
- `crecimiento-financiero-global/`, `crecimientofinancieroglobal.com/` — web principal de CFG.
- `cfg-seguros/` — web corporativa cfg-seguros.com (ramo seguros).
- `cfg-backend/`, `cfg-endpoint/`, `form-endpoint/`, `form-handler/` — backend y formularios de contacto.
- `cfg-restauracion/`, `deploy-cfg-limpio/`, `deploy-netlify/` — despliegues y restauraciones.
- `sandra-galilea/` — material Grupo Galilea.

**Club Contable (Colombia):**
- `clubcontable/`, `club-contable/`, `contabilidad/` — plataforma clubcontable.com (gestión de tareas contables por empresa).

**Otros:**
- `sandra-tech/` — proyecto/marca SandraTech.
- `Fivver/` — trabajos de Fiverr (apps, clientes, entregas, facturas, gigs, plantillas, recursos). Panel de todos sus trabajos.
- `proyectos/` — proyectos varios.
- `pendientes/` — tareas pendientes.

**Credenciales y respaldos (SENSIBLE — nunca las pegues en el chat):**
- `CONTRASEÑAS/`, `.creds/` (incluye `cloudflare.json`), `credenciales.md`, `CLAVES.md` — contraseñas y llaves de Sandra.
- `backup-web-*` — respaldos de versiones de la web.

**Tu memoria y diario:**
- `MEMORY.md` (este archivo) — tu memoria permanente que se carga sola.
- `memory/AAAA-MM-DD.md` — tu DIARIO por día: cada día registra lo que hiciste. Consúltalo para el historial detallado.
- `MEMORIA_VIVA.md`, `TABLERO.md`, `PROYECTOS.md`, `RESUMEN.md` — notas; consolida lo importante AQUÍ en MEMORY.md.

## Historial (resumen — detalle completo en memory/AAAA-MM-DD.md)
- **17 jun:** configuración de voz (TTS).
- **21 jun:** arranque — Sandra (Grupo Galilea, Madrid), primera póliza vendida, montar presencia online.
- **26–28 jun:** web crecimientofinancieroglobal.com montada (DNS, logo, formularios, Surge.sh) — funcionando.
- **29 jun – 1 jul:** revisiones, ajustes, CFG seguros.
- **jul:** CFG seguros, Club Contable y Fiverr en marcha.
- Para CUALQUIER detalle de una fecha, abre `memory/AAAA-MM-DD.md`.

==================== ESTADO ACTUAL DE PROYECTOS (MEMORIA VIVA) ====================

# MEMORIA VIVA - Estado de Proyectos

Última actualización: **Sábado 18 Julio 2026** (día masivo)

---

## 🔵 CFG — Crecimiento Financiero Global (dejado aparcado)
**Última sesión:** 16 julio 2026

### Estado actual
- Web crecimientofinancieroglobal.com aún servida por Worker de Cloudflare (yellow-bar-eceb)
- **DECISIÓN TOMADA:** Se dejó este sitio aparcado porque el formulario daba problemas
- El foco se movió a **cfg-seguros.com** donde se montó todo desde cero y funciona correctamente
- El sitio se queda como está, sin más cambios

### Nota importante
No tocar ni intentar arreglar el formulario de crecimientofinancieroglobal.com. El proyecto vivo de CFG ahora es cfg-seguros.com.

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

## 🟢 cfg-seguros.com — COMPLETO ✅

### Web
- ✅ cfg-seguros.com funcionando al 100%
- ✅ 16 páginas: Home, Privacidad, Aviso Legal, 6 seguros, 5 blog, redirect
- ✅ Formulario Web3Forms → info@cfg-seguros.com + Telegram
- ✅ Botón WhatsApp flotante (wa.me/+34641754490)
- ✅ Iconos redondos redes sociales (IG, FB, LinkedIn, TikTok)
- ✅ Footer limpio con enlaces legales
- ✅ Favicon en todas las páginas
- ✅ Deploy automático GitHub → Cloudflare Pages
- ✅ Google Search Console verificado
- ⏳ Google Business Profile en revisión (esperando carta)
- 📁 Código: cfg-seguros/ | Repo: sandluc22/cfg-seguros (master)

### Redes Sociales
| Red | Usuario | Estado |
|-----|---------|--------|
| Instagram | @cfg_seguros_gg | ✅ 7 posts, lanzamiento publicado |
| Facebook | CFG Seguros | ✅ WhatsApp integrado, 7 posts |
| LinkedIn | company/cfg-seguros | ✅ Creada, 3 posts, banner |
| TikTok | @cfgsegurosgg | ✅ Creada, logo, 2 vídeos |

### 📁 Archivos clave
- Ficha técnica PDF: proyectos/CFG/FICHA_CFG_SEGUROS.pdf
- Posts FB: proyectos/CFG/redes/facebook/
- Posts LinkedIn: proyectos/CFG/redes/linkedin/
- Vídeos TikTok: proyectos/CFG/redes/tiktok/

### ⏰ Recordatorios activos
- ✅ Saludo diario 6:30h
- ✅ Publicar redes lun/mié/vie 6:30h
- ✅ Cierre del día 22:30h

### 🔜 Próximo paso importante
Supervende (chatbot WhatsApp)

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

## ⏭️ Próximos pasos (Sábado 18 Jul)
1. ✅ Recordatorio redes configurado (lun/mié/vie 6:30h)
2. Seguir con posts de redes CFG Seguros
3. Decidir hosting para Club Contable + claves Namecheap
4. Preguntar detalles del taller

==================== SEGUIMIENTO CON SANDRA ====================

# 📋 SEGUIR CON SANDRA

> Archivo de referencia para retomar proyectos. Leer siempre antes de empezar a trabajar.

---

## 🏢 Club Contable

**Estado:** ⏸️ Publicado pero con versión antigua

### 🌐 Datos técnicos actuales
| Concepto | Estado |
|----------|--------|
| **Dominio** | clubcontable.com ✅ |
| **SSL** | ✅ Válido hasta 12 oct 2026 (Cloudflare)
| **TLS** | 1.3 con AES-256 ✅
| **Hosting** | Cloudflare (proyecto clubcontable-web) |
| **Caché** | Cloudflare cachea el HTML |
| **DNS** | 188.114.96.3 (Cloudflare) ✅ |
| **Web funcionando** | Sí, responde HTTP 200 ✅ |
| **Versión publicada** | ❌ ANTIGUA — sin cambios de categorías ni subcategorías |
| **Google Search Console** | Por verificar |
| **Google Business Profile** | Por verificar |

### 📄 Cambios realizados (no publicados)
- ✅ Categorías reordenadas (Contabilidad → Impuestos → Laboral → ReporteEntidades → SolicitudÁreas → Visitas → General)
- ✅ Subcategorías reordenadas dentro de cada categoría
- ✅ Selector de categorías dinámico en formulario
- ✅ Selector de subcategorías vinculado a categoría
- ✅ Opción "➕ Nueva categoría..." y "➕ Nueva subcategoría..."
- ✅ Protección admin (contraseña default: admin2025)
- ✅ Persistencia en localStorage
- ✅ Las tareas guardan subcategoría
- ✅ Filtro de búsqueda incluye categorías personalizadas
- ✅ Archivo en GitHub listo para publicar

### 📍 Código fuente
- **Workspace:** `/home/node/workspace/clubcontable/codigo/index.html`
- **GitHub:** https://github.com/SandraCaicedo/clubcontable/blob/main/codigo/index.html (versión actualizada)
- **Cloudflare:** proyecto `clubcontable-web` (versión antigua publicada)

### ⚠️ Problema detectado
El dominio clubcontable.com **sirve la versión antigua** del index.html. Los cambios de categorías y funcionalidades nuevas no están publicados. Hay que subir el nuevo index.html a Cloudflare.

### 📋 Pendientes
| # | Tarea | Estado |
|---|-------|--------|
| 1 | Subir nuevo index.html a Cloudflare (versión con categorías reordenadas) | ❌ Pendiente |
| 2 | Purgar caché de Cloudflare después del deploy | ❌ Pendiente |
| 3 | Verificar que todo funciona en clubcontable.com | ❌ Pendiente |
| 4 | Conectar GitHub con Cloudflare (deploy automático) | ❌ Pendiente |
| 5 | Configurar Google Search Console para clubcontable.com | 📝 Por definir |
| 6 | Configurar Google Business Profile | 📝 Por definir |

**Para seguir:** Necesito acceso a Cloudflare (token o panel) para subir el archivo nuevo. El código actualizado está en el workspace y en GitHub.

---

## 🏢 CFG-SEGUROS — CORREDORA DE SEGUROS

**Estado:** ✅ Web publicada y funcionando

### 🌐 Datos generales
- **Dominio:** cfg-seguros.com ✅
- **Cloudflare Pages:** Sí, proyecto `cfg-seguros-web`
- **SSL:** Sí (Cloudflare)
- **URL pages.dev:** https://cfg-seguros-web.pages.dev
- **Account ID:** `72305fb85467e89da2940e359f9e09cc`
- **Zone ID:** `9986e3c1cb4dd72f25ba56ec9afdb727`

### 📍 Código fuente
- **Workspace:** `/home/node/workspace/cfg-seguros/`
- **GitHub:** https://github.com/sandluc22/cfg-seguros (rama master) ✅

### 📄 Estructura del sitio (12 páginas)
```
cfg-seguros.com/
├── index.html                    — Home
├── seguros/
│   ├── index.html                — Listado
│   ├── vida.html
│   ├── salud.html
│   ├── hogar.html
│   ├── coche.html
│   ├── empresas.html
│   └── ahorro-inversion.html
└── blog/
    ├── index.html
    ├── seguro-vida-mitos-realidades.html
    ├── seguro-salud-guia-completa.html
    ├── proteccion-empresas-autonomos.html
    └── ahorro-inversion-primeros-pasos.html
```

### ⚙️ Sistema
- **Hosting:** Cloudflare Pages (proyecto cfg-seguros-web)
- **Formularios:** Web3Forms → leads llegan a info@cfg-seguros.com + Telegram ✅
- **Correos:** Migadu (info@cfg-seguros.com, ventas@cfg-seguros.com) ✅
- **Google Search Console:** Dominio verificado ✅
- **Google Business Profile:** En revisión ⏳ (esperando carta física)

### 📋 Estado de tareas
| # | Tarea | Estado |
|---|-------|--------|
| 1 | Web cfg-seguros.com funcionando | ✅ |
| 2 | Formulario captando leads (Web3Forms) | ✅ |
| 3 | Correos corporativos (info, ventas) en Migadu | ✅ |
| 4 | Google Search Console — dominio verificado | ✅ |
| 5 | Google Business Profile — en revisión | ⏳ |
| 6 | Conexión automática GitHub → Cloudflare | ❌ No configurado |

---

## 📁 Proyectos que aparezcan

*(En cuanto Sandra mencione un proyecto nuevo, lo añado aquí con su ficha)*

---

## ⚙️ Cómo funciona esto

- **Al empezar a hablar con Sandra**, Alfa lee este archivo primero para saber dónde se quedó.
- Las fichas se actualizan al final de cada bloque de trabajo.
- Cada ficha tiene: estado, avances, pendientes y cómo seguir.

==================== PROYECTOS ====================

# 📁 Proyectos de Sandra

**Última actualización:** 12-jul-2026

## CFG — Crecimiento Financiero Global
- **Web:** crecimientofinancieroglobal.com
- **Hosting:** Cloudflare Worker (yellow-bar-eceb)
- **Estado:** ⏸️ **APARCADO** — el proyecto vivo ahora es cfg-seguros.com
- **Nota:** formulario no funcional, no tocar

## CFG-SEGUROS (CORREDORA DE SEGUROS)
- **Web:** cfg-seguros.com ✅
- **Hosting:** Cloudflare Pages
- **Formulario:** Web3Forms funcionando
- **Correos:** Migadu (info, ventas)
- **Google Search Console:** Verificado
- **Estado:** ✅ Activo y operativo

## Club Contable
- **Web:** clubcontable.com | frontend: clubcontable.surge.sh
- **Hosting frontend:** Surge / **Backend:** Railway (caído)
- **Repo:** GitHub sandluc22/clubcontable
- **Config detallada:** ver `proyectos/Club Contable/FICHA.md`
- **Estado:** 🟡 Pendiente redeploy backend

## Fiverr — Perfil Freelancer
- **Usuario:** sandraluciac
- **Estado registro:** ✅ Vendedora activa (10/12 perfil)
- **Gig creado:** Diseño Web + Redes Sociales ($25-$120)
- **Pendiente:** Verificar identidad + Form W-9 para publicar
- **Config detallada:** ver `proyectos/Fiverr/FICHA.md`
