# MEMORY.md — Memoria permanente de Sandra

> Esta es tu memoria permanente y el ÚNICO archivo de memoria que se carga solo en cada sesión. Mantenla SIEMPRE al día. Aquí está el mapa de TODO tu trabajo; los detalles viven en las carpetas y en tu diario `memory/AAAA-MM-DD.md`.

## Quién es Sandra
Sandra Caicedo — agente de **Grupo Galilea** (seguros, ahorro e inversión) en Madrid, opera en toda España. Vendió su primera póliza y está montando su presencia online desde cero; dispone de ~2h/semana. También lleva **Club Contable** (Colombia). Tú eres **Alfa**, su asistente autónomo.

## Mapa de tu espacio de trabajo (/home/node/workspace)
Cuando trabajes en algo, ENTRA a la carpeta correspondiente y revisa/actualiza sus archivos. Todo esto ya existe:

**Seguros — CFG / Grupo Galilea (lo principal):**
- `crecimiento-financiero-global/`, `crecimientofinancieroglobal.com/` — web principal de CFG (APARCADA)
- `cfg-seguros/` — web corporativa cfg-seguros.com (ramo seguros) ✅ COMPLETO
- `cfg-backend/`, `cfg-endpoint/`, `form-endpoint/`, `form-handler/` — backend y formularios de contacto
- `cfg-restauracion/`, `deploy-cfg-limpio/`, `deploy-netlify/` — despliegues y restauraciones
- `sandra-galilea/` — material Grupo Galilea

**Club Contable (Colombia):**
- `clubcontable/` — plataforma clubcontable.com con backend Cloudflare Workers + D1
- `club-contable/`, `contabilidad/` — versiones anteriores

**Otros:**
- `sandra-tech/` — proyecto/marca SandraTech
- `Fivver/` — trabajos de Fiverr
- `proyectos/` — proyectos varios
- `pendientes/` — tareas pendientes

**Credenciales y respaldos (SENSIBLE — nunca las pegues en el chat):**
- `CONTRASEÑAS/`, `.creds/` (incluye `cloudflare.json`), `credenciales.md`, `CLAVES.md`
- `backup-web-*` — respaldos

**Tu memoria y diario:**
- `MEMORY.md` (este archivo)
- `memory/AAAA-MM-DD.md` — tu DIARIO por día

## Historial (resumen)
- **17 jun:** configuración de voz (TTS)
- **21 jun:** arranque — Sandra (Grupo Galilea, Madrid)
- **26–28 jun:** web crecimientofinancieroglobal.com montada
- **29 jun – 1 jul:** revisiones, ajustes, CFG seguros
- **jul:** CFG seguros, Club Contable y Fiverr en marcha
- **18 jul:** Club Contable: Backend D1 completo, frontend con login real, panel admin y reportes (pendiente arreglar diseño), selector de usuario en tareas, permisos admin/usuario
- **19 jul:** Club Contable MULTIEMPRESA ✅ — Backend v2 con empresas, frontend con selector de empresa, correos Migadu para clubcontable.com creados

==================== ESTADO ACTUAL DE PROYECTOS ====================

---

## 🔵 CFG — Crecimiento Financiero Global (APARCADO)
**No tocar.** Proyecto vivo es cfg-seguros.com.

---

## 🟢 cfg-seguros.com — COMPLETO ✅

### Web
- ✅ cfg-seguros.com funcionando al 100%
- ✅ 16 páginas, formulario Web3Forms, WhatsApp flotante
- ✅ Redes sociales: IG @cfg_seguros_gg, FB CFG Seguros, LinkedIn cfg-seguros, TikTok @cfgsegurosgg
- ✅ Google Search Console verificado
- ⏳ Google Business Profile en revisión (esperando carta)
- ✅ Deploy automático GitHub → Cloudflare Pages
- ✅ Supervende (bot "Lucía") configurado y activo

### Recordatorios (CAÍDOS)
- ❌ Saludo diario 6:30h — NO activo (se perdió)
- ❌ Publicar redes lun/mié/vie 6:30h — NO activo (se perdió)
- ❌ Cierre del día 22:30h — NO activo (se perdió)
- ⚠️ Los cron jobs se perdieron. Para la próxima tanda de posts, programarlos manualmente.

### Días de publicación
- **LUNES, MIÉRCOLES, VIERNES a las 6:30h (hora España)** — Publicar posts + TikTok
- Contenido FRESCO cada tanda: cambiar imágenes, colores y enfoque
- PRÓXIMA: miércoles 22 julio 6:30h
- **VIERNES 20:00h** — Revisar seguidores CFG Seguros

### Repositorio
- GitHub: sandluc22/cfg-seguros (master) → Cloudflare Pages

---

## 🎬 Videos CFG — CREADOS (21 jul 2026)

### Método final
- **ffmpeg + imágenes Unsplash** (1080x1920 vertical, 4-5s, H.264)
- Texto blanco con borde negro + headline dorado #f5a623 + dominio abajo
- Imágenes reales de fondo descargadas de Unsplash

### Videos generados y enviados (7 total)

**CFG Global** (crecimientofinancieroglobal.com):
1. 🏡 Hipoteca — "AHORRA HASTA 150€/MES" ✅
2. 💰 Cuentas — "HASTA 3.5% TAE" ✅
3. ✈️ Viajes — "VUELO+HOTEL POR 200€" ✅
4. 🎓 Estudios — "DESDE COLOMBIA ES POSIBLE" ✅ (fondo degradado, Unsplash bloqueó)

**CFG Seguros** (cfg-seguros.com):
5. ❤️ Vida — "SEGURO DE VIDA 5€/MES" ✅
6. 🏥 Salud — "ACCESO A CLÍNICAS PRIVADAS" ✅
7. 🏠 Hogar — "COBERTURA TOTAL" ✅
- ⚠️ **Corrección**: quitados precios de seguros (no son reales, cada caso es distinto)

### Problemas detectados
- ✅ **Dominio cfg-global.com no existe** → corregido a crecimientofinancieroglobal.com
- ✅ **Unsplash bloquea descargas** → algunas imágenes no se pudieron usar (estudios, viajes tuvieron que redescargarse)
- ✅ **Fondos degradados** son los que Sandra llama "feos" — los que tienen imagen real de fondo sí le gustan
- ✅ **Envío por Telegram** fallaba por archivos corruptos de 0 bytes

### Herramientas usadas
- ffmpeg (motor principal)
- ImageMagick convert (redimensionar imágenes)
- Unsplash (fotos de stock)
- Pexels (vídeos de stock con movimiento real)

### Futuro: vídeos con movimiento
Sandra quiere en el futuro vídeos con **personas moviéndose** (no foto estática). Opciones:
1. **CapCut móvil** (gratis) — ella desde el móvil
2. **RenderForest** (~10€/mes) — accesible desde servidor, sin Cloudflare
3. **Canva Pro** (~13€/mes)
4. **Pexels/Videvo** + ffmpeg — vídeos reales de stock montados con texto

Ficha técnica completa: `/home/node/workspace/videos/FICHA_TECNICA.md`
Ubicación: `/home/node/workspace/videos/para_enviar/`

---

## 🟢 Club Contable — MULTIEMPRESA ✅

### Estado actual (19 jul)
- ✅ **API backend v2** con multiempresa, desplegado en Cloudflare Worker
- ✅ Worker: `clubcontable-api` (ES module, binding D1 directo desde wrangler)
- ✅ D1 database `clubcontable-db` (categorias, subcategorias, tareas, usuarios, empresas, usuario_empresas)
- ✅ Login funcional: admin@clubcontable.com / admin2025
- ✅ URL API: https://clubcontable-api.crecimientofinancieroglobal.workers.dev
- ✅ **Multiempresa**: selector en header, tareas filtradas por empresa, crear tarea con empresa asignada
- ✅ Admin puede crear empresas para cualquier usuario
- ✅ Límite de empresas por usuario (según plan: default 3, admin ilimitado)
- ✅ Reportes filtrados por empresa
- ✅ Frontend desplegado en clubcontable.com (Cloudflare Pages, auto-deploy desde GitHub)

### Migadu — Correos clubcontable.com
- ✅ Dominio clubcontable.com activado en Migadu
- ✅ DNS configurado: TXT Verificación, DKIM, SPF, DMARC
- ✅ info@clubcontable.com
- ✅ ventas@clubcontable.com
- ✅ soporte@clubcontable.com
- ✅ financiero@clubcontable.com

### Repositorio
- GitHub: sandluc22/clubcontable (master) → Cloudflare Pages (frontend `clubcontable-front`) + Worker (`clubcontable-api`)
- Token CF (Workers + D1): `cfut_r8vBSU2267SoydiyswYKNJrDdbTpvDAZbtomE3EX3eff18ac`
- Account ID: `72305fb85467e89da2940e359f9e09cc`
- Worker URL: https://clubcontable-api.crecimientofinancieroglobal.workers.dev
- Web: https://clubcontable.com
- Login: admin@clubcontable.com / admin2025

## ✈️ Aviación TikTok (marido de Sandra)
- **Carpeta:** `/home/node/workspace/aviacion/`
- **10 vídeos creados** (todos, del 1 al 10)
- **Tema:** Aviación, historia, curiosidades, mitos
- **Formato:** 9s cada uno, 3 frames de 3s, overlay oscuro, textos blancos/azules
- **Ficha técnica:** `aviacion/FICHA_TECNICA.md`
- **Guía de guiones:** `aviacion/GUIA_10_VIDEOS.md`
- **Frames originales:** `aviacion/frames/video1/` a `video10/`
- **Recomendación:** Publicar 1-2 vídeos/día durante 14 días
- **Fecha creación:** 20 julio 2026

### Pendientes
1. ✅ **Login arreglado** — compatibility_date 2024-09-23
2. ✅ **Diseño Cloudflare** — sidebar izquierdo completado
3. ✅ **Colores CFG** — azul + amarillo aplicados
4. ⏳ **Sandra probar** clubcontable.com desde móvil/PC con Ctrl+Shift+R
5. ⏳ Nombre del producto (dentro de Club Contable como plataforma general)

---

## 🟣 Gafi
- Marketing de afiliados — Sin empezar

---

## 🎨 diseño-y-video — Carpeta central de creación de contenido
- **Ubicación:** `/home/node/workspace/diseño-y-video/`
- Contiene: vídeos finales, fichas de herramientas, scripts
- **Ficha principal:** `FICHA_HERRAMIENTAS.md` — todas las herramientas que usamos
- **Script generación vídeos movimiento:** `generar_videos_movimiento.py` (en diseño-y-video/)
- **Vídeos finales (foto estática):** `videos/` — 7 vídeos CFG Global + Seguros
- **Vídeos con movimiento real:** `/home/node/workspace/videos-con-movimiento/` — 7 vídeos con Pexels + ffmpeg
- **Vídeos aviación:** `/home/node/workspace/aviacion/` — 10 vídeos para TikTok del marido

### Estado vídeos con movimiento (21 jul)
✅ Generados y enviados: Ahorro, Inversiones, Seguros, Salud, Hogar (casa zoom), Viajes
❌ **Estudios: PENDIENTE** — Sandra no ha encontrado una foto que le guste. Pendiente que ella elija desde Pexels.
✅ Formato definitivo: 7-10s, 720x1280, texto blanco 44px con borde negro 4px, SIN dominio en pantalla
✅ Scripts guardados en diseño-y-video/
✅ FICHA_HERRAMIENTAS.md actualizada

## 🟠 Gestión de taller
- Sandra lo mencionó sin detalles — Pendiente preguntar

---

## 📧 Migadu
- ✅ info@crecimientofinancieroglobal.com funcionando
- ✅ info@cfg-seguros.com funcionando
- ✅ ventas@cfg-seguros.com funcionando
- ✅ clubcontable.com activado con correos (info, ventas, soporte, financiero)
- ⏳ sandra@cfg-seguros.com — pendiente (Sandra dijo que lo hace ella)

---

## 🔐 Contraseñas
- Todo en `/home/node/workspace/CONTRASEÑAS/`
- Token Cloudflare guardado: `.creds/cloudflare.json` (cfut_Xz6X6IWIGSnzkyHCcPAyU4CxLjAtqoOo6ajOLekX26ac33a5 — Workers + D1)
- Token nuevo (19 jul): `cfut_9gozVyFmNgDvdYYowPqqkHWhctSQSzB9B3oiEW0fe37e9540` — sin Workers
- Token nuevo v2 (19 jul): `cfut_r8vBSU2267SoydiyswYKNJrDdbTpvDAZbtomE3EX3eff18ac` — Workers + D1 ✅
- Correo CFG: crecimientofinancieroglobal@gmail.com
- **Club Contable DB pass:** admin2025 (reseteada desde consola D1)

---

## 💰 Precios Club Contable (definidos 19 jul)
| Empresas | Precio COP/mes |
|---|---|
| Prueba 7 días | Gratis 🆓 |
| 1 empresa | $12.999 |
| 2-3 empresas | $19.999 |
| 4-10 empresas | $29.999 |
| +10 empresas | $39.999 |

## ⏭️ Próximos pasos
1. 🟡 **Arreglar login Club Contable** — error 1042 worker. Sandra revisa Compatibility Date en clubcontable-api → Settings → Runtime
2. ✅ Verificar diseño subcategorías dentro de categorías
3. Diseño tipo Cloudflare (menú lateral)
4. Ajustes móvil
5. Publicar redes CFG Seguros (lun/mié/vie)
6. sandra@cfg-seguros.com (pendiente Migadu)
7. **Viernes 20:00h** — estrategia seguidores CFG Seguros 🗓️

### ☁️ crecimientofinancieroglobal.com — DESPLEGADA ✅ (21 jul)
- ✅ Proyecto Pages: **cfg-global-web** (ya existía)
- ✅ Dominio **crecimientofinancieroglobal.com** conectado y activo
- ✅ Deploy forzado con 11 artículos SEO
- ✅ SSL automático de Cloudflare
- ⏳ Esperar a que financeAds revise

### Token nuevo (21 jul)
- Token con Pages+Workers+D1: `cfut_akHw0gDJIRuumDTPY13MCvX7M0OsYtrnmQE3l5sga18b4821`
- Guardado en `.creds/cloudflare.json` como `token_pages_2026_07_21`

### 🆕 crecimientofinancieroglobal.com — COMPLETO ✅ (21 jul)
- ✅ Limpieza total de archivos basura
- ✅ Index reescrito con 7 categorías (financieros, hipotecas, seguros, coches, viajes, formación, estudiar españa)
- ✅ Repositorio GitHub: sandluc22/crecimientofinancieroglobal (master)
- ✅ Cloudflare Pages conectado (deploy automático)
- ✅ Dominio: crecimientofinancieroglobal.com
- ✅ Google Search Console verificado + sitemap enviado
- ✅ Google Analytics GA4 (G-XVVBY349WZ) instalado
- ✅ Logo subido, rediseño visual, botones presupuesto
- ✅ Seguros enlazados a cfg-seguros.com
- ✅ Sin Sandra/Galilea en contacto
- ✅ Estudiar España con contenido LATAM (homologación, visados, universidades)
- ✅ Páginas legales: Aviso Legal + Privacidad
- ✅ Ficha técnica actualizada
- ⏳ Pendiente: escribir artículos SEO periódicos

### 🆕 Worker v2 — CRUD completo (20 jul)
- ✅ Worker reescrito con todas las rutas: login, tareas (GET+POST+DELETE), categorías (GET+POST+DELETE), subcategorías (GET+POST+DELETE), dashboard, empresas (GET)
- ✅ Formato respuesta: `{ok: true, result: [...]}` 
- ✅ Token nuevo guardado: `cfut_OxEyLlBS3w5Z9sSTKBMdcwNOMjynQRKj0wFNkPD313109f57`
- ✅ Desplegado en clubcontable-api.crecimientofinancieroglobal.workers.dev (versión activa 8578d03f al 100%)
- ✅ Frontend actualizado con colores CFG (azul #2563eb + amarillo hover), sidebar con 5 secciones (Dashboard, Tareas, Categorías, Subcategorías, Reportes), CRUD completo desde el frontend, dashboard, reportes por categoría
- ✅ Cloudflare Pages deploy automático desde GitHub (clubcontable-front)

### Token Cloudflare actual
- Token Workers + D1: `cfut_OxEyLlBS3w5Z9sSTKBMdcwNOMjynQRKj0wFNkPD313109f57`

## 🗓️ 20 julio 2026 — Jornada maratónica Club Contable

### Qué se hizo
- **Worker v2 completo**: reescrito con rutas CRUD (tareas, categorías, subcategorías), dashboard, empresas (GET+POST), usuarios (GET+POST solo admin)
- **Worker desplegado** exitosamente en clubcontable-api (versión 8578d03f activa al 100%)
- **Token nuevo guardado**: `cfut_OxEyLlBS3w5Z9sSTKBMdcwNOMjynQRKj0wFNkPD313109f57`
- **Frontend reescrito 3 veces** hasta quedar con:
  - Sidebar oscuro (#1e293b), azul (#2563eb), hover amarillo (#f59e0b)
  - Dashboard, Tareas, Categorías, Subcategorías, Reportes, Admin (sidebar 6 secciones)
  - Selectores funcionales con datos cargados desde API
  - Panel Admin: crear usuarios y empresas
  - Dashboard con % de cumplimiento + barra de progreso
  - Reportes por categoría y empresa con porcentajes
- **Último push**: commit `a64c0bc` "Frontend completo CFG + worker v2 CRUD + limpieza archivos basura"
- **FICHA_TECNICA.md** creada en `/home/node/workspace/clubcontable/FICHA_TECNICA.md`
- **Diario guardado** en `memory/2026-07-20.md`

### Problemas del día
- El api token `cfut_OxEy...` NO permite `wrangler versions deploy` (solo create). Necesito un API Token con permisos más amplios para poder activar versiones desde CLI.
- El frontend tardó en tener los colores porque Cloudflare Pages no refresca automáticamente o no se configuraba bien.
- Login falló varias veces porque la contraseña contenía caracteres que se escapaban mal en shell.
- **Clubcontable.com no se ve con colores CFG desde el navegador de Sandra** (posible caché o Pages no actualizado)

### Pendientes REALES
1. 🟡 **Verificar clubcontable.com desde casa de Sandra** — si en modo incógnito no se ven los colores azul/amarillo ni el sidebar oscuro, el deploy de Pages no se ha completado o hay error de configuración
2. ✅ Verificar diseño subcategorías dentro de categorías
3. ✅ Diseño tipo Cloudflare (menú lateral)
4. ✅ Ajustes móvil
5. ✅ Publicar redes CFG Seguros (lun/mié/vie)
6. ⏳ sandra@cfg-seguros.com (pendiente Migadu)
7. 🗓️ **Viernes 20:00h** — revisar seguidores CFG Seguros

---

## 🗓️ 20 julio 2026 — Jornada maratónica Club Contable

### Qué se hizo
- **Worker v2 completo**: reescrito con rutas CRUD (tareas, categorías, subcategorías), dashboard, empresas (GET+POST), usuarios (GET+POST solo admin)
- **Worker desplegado** exitosamente en clubcontable-api (versión 8578d03f activa al 100%)
- **Token nuevo guardado**: `cfut_OxEyLlBS3w5Z9sSTKBMdcwNOMjynQRKj0wFNkPD313109f57`
- **Frontend reescrito 3 veces** hasta quedar con:
  - Sidebar oscuro (#1e293b), azul (#2563eb), hover amarillo (#f59e0b)
  - Dashboard, Tareas, Categorías, Subcategorías, Reportes, Admin (sidebar 6 secciones)
  - Selectores funcionales con datos cargados desde API
  - Panel Admin: crear usuarios y empresas
  - Dashboard con % de cumplimiento + barra de progreso
  - Reportes por categoría y empresa con porcentajes
- **Último push**: commit `4beb67f` "Frontend completo con colores CFG..."

### Problemas del día
- El api token `cfut_OxEy...` NO permite `wrangler versions deploy` (solo create). Necesito un API Token con permisos más amplios para poder activar versiones desde CLI.
- El frontend tardó en tener los colores porque Cloudflare Pages no refresca automáticamente o no se configuraba bien.
- Login falló varias veces porque la contraseña contenía caracteres que se escapaban mal en shell.

## 🎯 ESTRATEGIA GLOBAL — Meta: 300.000€ para la casa 🏠

> **Objetivo:** Casa cerca del Estadio Metropolitano (Atlético de Madrid), ~300.000€

### Filosofía
Todo lo que hacemos está encaminado a **generar ingresos reales**. No montar webs por montar. Cada proyecto tiene que convertirse en una fuente de dinero.

### CFG Seguros (el producto que ya existe)
- Las pólizas ya existen (Grupo Galilea), la web está montada, redes creadas
- Fase actual: **darle caña a tráfico y seguidores** para convertirlos en clientes
- Es la vía más rápida porque ya hay comisiones directas
- Publicar lun/mié/vie 6:30h
- Viernes 20:00h revisar seguidores

### crecimientofinancieroglobal.com — ESTRATEGIA DE AFILIADOS 🚀

**Concepto:** Web tipo **directorio + blog SEO**. Cada categoría es un "canasto" con sus enlaces de afiliado.

**Las categorías ("canastos"):**
| Categoría | Productos afiliados | Ejemplos |
|---|---|---|
| 💰 Productos Financieros | Cuentas, depósitos, inversiones | Trade Republic, MyInvestor, Rankia |
| 🏡 Hipotecas | Comparativas, simuladores | Hipotecas.com, bancos |
| 🛡️ Seguros | Tus pólizas de CFG | Grupo Galilea |
| 🚗 Coches | Alquiler y compra | DiscoverCars, Rentalcars |
| ✈️ Viajes | Vuelos, hoteles, alquiler coches | Booking, Skyscanner |
| 📚 Formación | Cursos, libros, membresías | Hotmart, Amazon |

**Estrategia SEO (cómo llega la gente):**
- Escribir artículos que respondan a búsquedas reales:
  - "¿Qué banco da la mejor hipoteca en 2026?"
  - "¿Dónde alquilar coche barato en Madrid?"
  - "Mejores cursos de finanzas online"
  - "Seguro de vida: ¿merece la pena?"
- Google encuentra los artículos → la gente entra → ve los enlaces de afiliado → compra → Sandra cobra comisión

**Flujo de trabajo:**
1. Alfa escribe artículos SEO optimizados
2. Sube a la web (GitHub → deploy automático Cloudflare)
3. Sandra comparte en redes
4. Google indexa, la gente encuentra, compra, cobramos

### Club Contable — APARCADO (vuelta en unos días)
El producto se está construyendo, no está listo para vender. Se retomará cuando toque.

### Otros proyectos (secundarios / futuro)
- **Fiverr**: aparcado (demasiado trabajo inicial)
- **Libro de IA**: semilla, sin empezar
- **Gestión de taller**: pendiente definir
- **Aviación TikTok**: 10 vídeos listos para publicar (marido de Sandra)

---

## ⏭️ PRÓXIMOS PASOS (priorizados) — Actualizado 21 jul

### 🔴 Prioridad 1 — Vídeo de Estudios (PENDIENTE)
- ⏳ Sandra elige una foto de estudiantes desde Pexels y me pasa el enlace
- ⏳ Yo la descargo, pongo texto y genero el vídeo final
- ⏳ Una vez aprobado, actualizar los otros 6 vídeos con el mismo formato (sin dominio)

### 🔴 Prioridad 2 — crecimientofinancieroglobal.com
- ✅ Cloudflare Pages + deploy automático desde GitHub
- ✅ Index con 7 categorías + logo + rediseño visual
- ✅ Google Search Console verificado + sitemap enviado (30+ URLs)
- ✅ Google Analytics (G-XVVBY349WZ) instalado
- ✅ Estudiar España con contenido LATAM (homologación, visados, universidades)
- ✅ Aviso Legal + Privacidad
- ✅ Ficha técnica creada y en PDF
- ⏳ Pendiente: escribir artículos SEO periódicos

### 🟡 Prioridad 3 — CFG Seguros ✅ TÉCNICAMENTE COMPLETO
- ✅ Google Search Console verificado
- ✅ Google Analytics (G-XVVBY349WZ) instalado
- ✅ Sitemap.xml + robots.txt creados
- ✅ Ficha técnica creada y en PDF
- ⏳ Google Business Profile (pendiente carta física con código)
- ⏳ Publicar redes lun/mié/vie
- ⏳ sandra@cfg-seguros.com (Migadu, lo hace Sandra)

### 🟡 Prioridad 4 — Elegir primer programa de afiliados
- ⏳ Pendiente respuesta de financeAds
- Decidir entre: hipotecas, coches (DiscoverCars/Rentalcars), Hotmart (formación/finanzas)

### 🟡 Prioridad 5 — Club Contable (vuelta más adelante)
- Verificar que clubcontable.com muestra colores CFG
- Añadir filtros de reportes por rango de fechas
- Panel Admin: asignar empresa a usuario
