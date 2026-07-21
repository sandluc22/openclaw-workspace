# ✈️ FICHA TÉCNICA — CANAL DE AVIACIÓN PARA CURIOSOS

> **Para:** El marido de Sandra
> **Creado por:** Alfa (asistente de Sandra)
> **Fecha:** 20 julio 2026

---

## 📐 FORMATO DE LOS VÍDEOS

| Característica | Valor |
|---|---|
| **Formato** | Vertical 9:16 |
| **Resolución** | 1080x1920 px |
| **Duración** | ~9 segundos (3 frames de 3s cada uno) |
| **FPS** | 30 |
| **Códec** | H.264 |
| **Peso aprox.** | 400-850 KB por vídeo |
| **Estilo** | Imagen de fondo + overlay oscuro (30-35%) + texto en pantalla |

## 🎨 DISEÑO DE CADA FRAME

### Barra superior
- **Fondo:** Negro sólido
- **Altura:** 140px
- **Texto 1:** "✈️ AVIACIÓN — HISTORIA Y CURIOSIDADES" (o "✈️ AVIACIÓN PARA CURIOSOS") en AZUL (0,150,255)
- **Texto 2:** "Datos que te sorprenderán" en GRIS (200,200,200)

### Cuerpo
- **Icono grande** centrado (🌍📖✈️🏆🔥 etc.) posición Y=300
- **Título principal** en BLANCO, fuente LiberationSans-Bold 60px, centrado, Y desde 430
- **Texto secundario** en GRIS, fuente 36px, centrado

### Pie
- **CTA:** "📲 Sígueme para más aviación" en AZUL (0,150,255), posición Y=1750

### Overlay
- Capa negra al 30-35% de opacidad sobre la imagen de fondo

## 📦 ESTRUCTURA DE LA CARPETA

```
aviacion/
├── FICHA_TECNICA.md          ← Este archivo
├── GUIA_10_VIDEOS.md         ← Guía con los 10 guiones escritos
├── video_aviacion_1.mp4      ← "Aviones no vuelan en línea recta"
├── video_aviacion_2.mp4      ← "Top 5 aviones más grandes"
├── video_aviacion_3.mp4      ← "5 datos curiosos de aviación"
├── video_aviacion_4.mp4      ← "El primer vuelo duró 12 segundos"
├── video_aviacion_5.mp4      ← "Cosas que no sabías sobre los pilotos"
├── video_aviacion_6.mp4      ← "Récords de aviación"
└── frames/
    ├── video1/               ← Frames PNG del vídeo 1
    ├── video2/               ← Frames PNG del vídeo 2
    ├── video3/               ← Frames PNG del vídeo 3
    ├── video4/               ← Frames PNG del vídeo 4
    ├── video5/               ← Frames PNG del vídeo 5
    └── video6/               ← Frames PNG del vídeo 6
```

## 📋 LISTA COMPLETA DE VÍDEOS (6 de 10 creados)

| # | Título | Tema | Duración | Estado |
|---|---|---|---|---|
| 1 | "Aviones no vuelan en línea recta" | Curiosidad | 9s | ✅ CREADO |
| 2 | "Top 5 aviones más grandes" | Ranking | 9s | ✅ CREADO |
| 3 | "5 datos curiosos de aviación" | Curiosidad | 9s | ✅ CREADO |
| 4 | "El primer vuelo duró 12 segundos" | Historia | 9s | ✅ CREADO |
| 5 | "Cosas que no sabías sobre los pilotos" | Curiosidad | 9s | ✅ CREADO |
| 6 | "Récords de aviación" | Récords | 9s | ✅ CREADO |
| 7 | "5 mitos sobre volar" | Mitos | - | 📝 Pendiente |
| 8 | "Aviones famosos de la historia" | Historia | - | 📝 Pendiente |
| 9 | "El aterrizaje más suave" | Visual | - | 📝 Pendiente |
| 10 | "Airbus vs Boeing" | Comparativa | - | 📝 Pendiente |

## 🖼️ FUENTES DE IMÁGENES

Las imágenes de fondo se descargan de **Unsplash** (banco de imágenes gratuito):
- URL base: `https://images.unsplash.com/photo-XXXXX?w=1080`
- Sin derechos de autor, uso comercial permitido
- Todas redimensionadas a 1080x1920

## 🛠️ CÓMO SE CREAN LOS VÍDEOS (PROCESO)

```
1. Buscar foto libre en Unsplash
2. Descargar con curl a 1080px de ancho
3. Usar Python + Pillow para crear el frame:
   - Abrir imagen → redimensionar a 1080x1920
   - Aplicar overlay negro al 30-35%
   - Dibujar barra superior, icono, título, texto y CTA
   - Guardar como PNG
4. Repetir 3 veces (3 frames por vídeo)
5. Usar ffmpeg para unir los 3 frames:
   ffmpeg -loop 1 -i frame1.png -c:v libx264 -t 3 ... (x3 frames)
   ffmpeg -f concat -i lista.txt -c copy video_final.mp4
```

## 📌 REGLAS PARA NO OLVIDAR

1. **Siempre 3 frames por vídeo**
2. **Cada frame 3 segundos** → total ~9s
3. **Overlay negro 30-35%**
4. **Fuentes:** LiberationSans Bold (títulos) y Regular (textos)
5. **Colores:** Blanco (#FFF), Azul (#0096FF), Gris (#C8C8C8)
6. **CTA siempre al final:** "📲 Sígueme para más aviación"
7. **Los vídeos deben pesar < 1MB** para que Telegram los acepte

## 🔄 PRÓXIMOS PASOS

- [ ] Completar los 4 vídeos restantes (7 al 10)
- [ ] Si el marido de Sandra consigue sus propias fotos, sustituir las de Unsplash
- [ ] Subir los vídeos a TikTok
- [ ] Publicar 1-2 vídeos al día durante 14 días

---

*Ficha creada el 20 julio 2026 por Alfa para Sandra*

---

## ✅ VÍDEOS COMPLETADOS (TODOS LOS 10)

| # | Título | Tema | Duración | Tamaño |
|---|---|---|---|---|
| 1 | "Aviones no vuelan en línea recta" | Curiosidad | 9s | 645 KB |
| 2 | "Top 5 aviones más grandes" | Ranking | 9s | 833 KB |
| 3 | "5 datos curiosos de aviación" | Curiosidad | 9s | 394 KB |
| 4 | "El primer vuelo duró 12 segundos" | Historia | 9s | 547 KB |
| 5 | "Cosas que no sabías sobre los pilotos" | Curiosidad | 9s | 658 KB |
| 6 | "Récords de aviación" | Récords | 9s | 740 KB |
| 7 | "5 mitos sobre volar" | Mitos | 9s | 493 KB |
| 8 | "Aviones que cambiaron la historia" | Historia | 9s | 528 KB |
| 9 | "¿Cómo aterriza sin rebotar?" | Técnica | 9s | 835 KB |
| 10 | "Airbus vs Boeing" | Comparativa | 9s | 712 KB |

**Todos los 10 vídeos enviados a Sandra por Telegram.** ✅
