# 🛠️ Ficha de herramientas — Diseño y Vídeo

> Actualizado: 21 julio 2026

---

## 📦 Estructura de carpetas

```
diseño-y-video/
├── FICHA_HERRAMIENTAS.md          ← Esta ficha
├── herramientas/
│   └── generar_frames.py          ← Script original de frames
├── videos/                        ← Vídeos primera tanda (foto estática, 7 piezas)
├── generar_videos_movimiento.py   ← Script generación vídeos con Pexels+ffmpeg
├── generar_estudios.py           ← Script específico para el de Estudios
├── generar_imagen_art.py         ← Generador de imágenes ilustradas (DESCARTADO)
└── generar_todos.sh              ← Script shell original
```

---

## 🎬 Pexels + ffmpeg — VÍDEOS CON MOVIMIENTO REAL ✅

**Estado:** ✅ FUNCIONANDO — método definitivo
**Motor principal:** ffmpeg
**API Pexels:** Key `8aQi8VBxjwqIWAwE0ZxfPrvm9TrKLCNNKFWWGG8X0EtLvWqOyoWZQcA8`
**Fuentes:** 
- Vídeos: API Pexels videos (queries limitadas: business, nature, technology, doctor, sea, people, success, sunset)
- Fotos: API Pexels photos (queries limitadas: nature, home, students, etc.)
- **⚠️ Pexels ya no deja descargar fotos libremente** — hay que pedirle a Sandra el enlace directo

### Script central
```bash
/home/node/workspace/diseño-y-video/generar_videos_movimiento.py
```

### IDs de Pexels VÁLIDOS para vídeos verticales (1080x1920 o 720x1280):

| ID | Tema | Resolución |
|---|---|---|
| 6326861 | Dinero/ahorro (hombre contando) | 1080x1920 |
| 38470559 | Trading/inversiones (tablet gráficos) | 1080x1920 |
| 7983988 | Negocios/empresa (oficina) | 1080x1920 |
| 7983985 | Negocios/empresa v2 | 1080x1920 |
| 7423714 | Doctor/salud (doctora paciente) | 1080x1920 |
| 6120371 | Éxito/escritorio (mujer escritorio) | 1080x1920 |
| 36906465 | Atardecer/viajes | 720x1280 |

### Asignación tema → vídeo:

| Tema | Archivo original | Texto | Dominio |
|---|---|---|---|
| Ahorro | dinero.mp4 | "AHORRA CON INTELIGENCIA" | crecimientofinancieroglobal.com |
| Inversiones | trading.mp4 | "INVIERTE CON CONFIANZA" | crecimientofinancieroglobal.com |
| Seguros/Vida | negocios.mp4 | "PROTEGE A TU FAMILIA" | cfg-seguros.com |
| Salud | salud.mp4 | "CUIDA TU SALUD" | cfg-seguros.com |
| Hogar | casa.jpg (foto, zoom) | "TU HOGAR PROTEGIDO" | cfg-seguros.com |
| Viajes | viajes.mp4 | "VIAJA TRANQUILO" | crecimientofinancieroglobal.com |
| Estudios | PENDIENTE (Sandra elige) | "ESTUDIA EN ESPANA" | crecimientofinancieroglobal.com |

### Formato de salida
- **Resolución:** 720x1280 (9:16 vertical)
- **Duración:** 7-10 segundos
- **Códec:** H.264
- **Texto:** Blanco con borde negro 4px, tamaño 44, centrado arriba
- **Dominio:** ❌ NO va en el vídeo — se pone en la descripción de TikTok/Reels/IG

### 📥 Descarga de vídeos desde Pexels
```bash
curl -L -o nombre.mp4 "https://videos.pexels.com/video-files/ID/ARCHIVO.mp4"
```
Los nombres de archivo exactos se obtienen de la API.

### ⚠️ Problemas conocidos
1. **Pexels API photos** — limitada tras muchas llamadas. Algunas queries devuelven 0 resultados.
2. **Pexels bloquea descarga directa** — las fotos llegan como AVIF en lugar de JPEG. Convertir con `PIL.Image`.
3. **Sandra no puede ver las imágenes** — hay que mostrarle y que ella confirme.
4. **Zoompan en ffmpeg** — puede colgarse si la imagen no tiene suficiente resolución.
5. **Vídeos originales perdidos** — hubo que redescargarlos. Mantener backup.

---

## 🎬 RenderForest ❌ DESCARTADO

- Cuenta creada: crecimientofinancieroglobal@gmail.com / CFGglobal2026!
- La versión gratuita NO renderiza vídeos finales descargables
- Filtro de contenido: bloquea términos como "ahorra dinero", "hipoteca", "ofertas"
- **Decisión:** No merece pagar 10€/mes teniendo Pexels+ffmpeg gratis

---

## 🛠️ Herramientas disponibles

| Herramienta | Estado | Uso |
|---|---|---|
| ffmpeg | ✅ Instalado | Motor principal de vídeo |
| ImageMagick | ✅ Instalado | Redimensionar imágenes |
| Python/PIL | ✅ Instalado | Convertir formatos, generar imágenes |
| Pexels API | ✅ Funciona (limitado) | Buscar vídeos y fotos de stock |
| Unsplash | ❌ Bloqueado | Descargas rechazadas desde servidor |

---

## 📁 Ubicación de archivos

- **Vídeos primera tanda (foto estática):** `/home/node/workspace/diseño-y-video/videos/`
- **Vídeos con movimiento real:** `/home/node/workspace/videos-con-movimiento/`
- **Vídeos aviación:** `/home/node/workspace/aviacion/`
- **Scripts:** `/home/node/workspace/diseño-y-video/`
- **Ficha técnica CFG Global:** `/home/node/workspace/crecimientofinancieroglobal.com/FICHA_TECNICA.md`
- **Ficha técnica CFG Seguros:** `/home/node/workspace/cfg-seguros/FICHA_TECNICA.md`
- **Ficha técnica Club Contable:** `/home/node/workspace/clubcontable/FICHA_TECNICA.md`
