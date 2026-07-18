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
- **Cloudflare Pages:** Sí, proyecto `cfg-seguros-web` (el real, intacto)
- **SSL:** Sí (Cloudflare)
- **URL pages.dev:** https://cfg-seguros-web.pages.dev
- **Account ID:** `72305fb85467e89da2940e359f9e09cc`
- **Zone ID:** `9986e3c1cb4dd72f25ba56ec9afdb727`

### 📍 Código fuente
- **Workspace (código real):** `/home/node/workspace/cfg-seguros/`
- **GitHub:** https://github.com/sandluc22/cfg-seguros (rama master) ✅ — TODO el código está ahí
- **README:** `/home/node/workspace/cfg-seguros/README.md`

### 📄 Estructura del sitio (12 páginas)
```
cfg-seguros.com/
├── index.html                    — Home
├── seguros/
│   ├── index.html                — Listado de seguros
│   ├── vida.html                 — Seguro de Vida
│   ├── salud.html                — Seguro de Salud
│   ├── hogar.html                — Seguro de Hogar
│   ├── coche.html                — Seguro de Coche
│   ├── empresas.html             — Seguro de Empresas
│   └── ahorro-inversion.html     — Ahorro e Inversión
└── blog/
    ├── index.html                — Índice del blog
    ├── seguro-vida-mitos-realidades.html
    ├── seguro-salud-guia-completa.html
    ├── proteccion-empresas-autonomos.html
    └── ahorro-inversion-primeros-pasos.html
```

### ⚙️ Sistema
- **Hosting:** Cloudflare Pages (proyecto cfg-seguros-web)
- **Formularios:** Captan leads → notificaciones a info@cfg-seguros.com + Telegram
- **Correos:** Migadu (info@cfg-seguros.com, ventas@cfg-seguros.com)
- **Google Search Console:** Dominio verificado ✅
- **Google Business Profile:** En revisión ⏳ (esperando carta física)

### 📋 Estado de tareas
| # | Tarea | Estado |
|---|-------|--------|
| 1 | Web cfg-seguros.com funcionando | ✅ |
| 2 | Formulario captando leads (email + Telegram) | ✅ |
| 3 | Correos corporativos (info, ventas) en Migadu | ✅ |
| 4 | Google Search Console — dominio verificado | ✅ |
| 5 | Sitemap enviado a Google | ✅ |
| 6 | Google Business Profile — en revisión | ⏳ |
| 7 | Conexión automática GitHub → Cloudflare | ❌ No configurado |
| 8 | Club Contable — revisar error en web | ⏸️ Pendiente |

---

## 📁 Proyectos que aparezcan

*(En cuanto Sandra mencione un proyecto nuevo, lo añado aquí con su ficha)*

---

## 🎯 Plan de Captación de Clientes — CFG-SEGUROS / Grupo Galilea

**Próxima sesión:** Sábado 18 de julio de 2026

### Estrategia gratuita definida
| # | Acción | Coste | Estado |
|---|-------|-------|--------|
| 1 | Google My Business — esperar carta y verificar | Gratis | ⏳ En espera |
| 2 | Instagram orgánico — contenido 2-3 veces/semana | Gratis | 📝 Pendiente |
| 3 | Grupos de Facebook Madrid — participar sin vender directo | Gratis | 📝 Pendiente |
| 4 | Blog de cfg-seguros.com — crear más artículos | Gratis | 📝 Pendiente |
| 5 | Google Ads / Facebook Ads (inversión única futura) | 50-70€ | 💤 Más adelante |

---

## ⚙️ Cómo funciona esto

- **Al empezar a hablar con Sandra**, Alfa lee este archivo primero para saber dónde se quedó.
- Las fichas se actualizan al final de cada bloque de trabajo.
- Cada ficha tiene: estado, avances, pendientes y cómo seguir.
