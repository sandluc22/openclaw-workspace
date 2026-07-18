# Club Contable · clubcontable.com

## Información general
- **Nombre:** Club Contable
- **País:** Colombia 🇨🇴
- **Descripción:** Plataforma interna de gestión de tareas contables por empresa y categoría
- **Dominio:** clubcontable.com
- **Registrador:** Namecheap (sandluc22)
- **Fecha de migración a Cloudflare:** Julio 2026

---

## Hosting
- **Plataforma:** Cloudflare Pages ✅ (migrado desde Netlify)
- **Proyecto:** clubcontable-web
- **URL producción:** https://clubcontable.com
- **URL pages.dev:** https://clubcontable-web.pages.dev
- **Account ID (Cloudflare):** 72305fb85467e89da2940e359f9e09cc
- **Zone ID (clubcontable.com):** 1f29ff229ec2d7cc6f23cc016c508c3b

## DNS (Cloudflare)
- **Nameservers:** burt.ns.cloudflare.com / liz.ns.cloudflare.com
- **CNAME @ →** clubcontable-web.pages.dev (Proxied 🟠)
- **CNAME www →** clubcontable-web.pages.dev (Proxied 🟠)
- **MX 10 →** aspmx1.migadu.com
- **MX 20 →** aspmx2.migadu.com

## SSL/TLS
- **Estado:** Activo (certificado universal automático de Cloudflare)
- **Tipo:** Full (strict)

---

## Usuarios del sistema

| Usuario | Nombre | Rol |
|---------|--------|-----|
| **sandra** | Sandra (Administradora) | 👑 Admin |
| **maria** | María Ángel | 👤 Usuario |
| **yurleny** | Yurleny | 👤 Usuario |
| **kareling** | Kareling | 👤 Usuario |

### Contraseñas
- Sandra: `Sandra2026`
- María Ángel: `Maria2026`
- Yurleny: `Yurleny2026`
- Kareling: `Kareling2026`

---

## Categorías del sistema

| Categoría | Subcategorías |
|-----------|---------------|
| 💰 **Impuestos** | IVA, Retefuente, Renta, Exógena, RUB, Reteica |
| 👷 **Laboral** | Seg. Social, Nómina |
| 📊 **Contabilidad** | Compras, Tesorería, Activos Fijos, Financiero, Facturación |
| 🏛️ **Reporte Entidades** | RNB, Supersociedades, Plan Maestro, Cámara Comercio, Otra |
| 🔍 **Visitas** | Revisoría, Aud. Régimen Franco, Aud. Sagrilatf, Otra |
| 📋 **Solicitud Áreas** | Accionistas, Gerencia Gral, Gerencia Admin/Fin, Operaciones, Of. Cumplimiento, Otra |

---

## Empresas registradas
El sistema permite gestionar tareas por empresa (NIT). La lista completa está en el código fuente (`codigo/index.html`).

---

## Estructura del proyecto

```
clubcontable/
├── README.md              ← Esta ficha
├── notas.md               ← Notas del proyecto (versión anterior)
└── codigo/
    └── index.html         ← App completa (login, categorías, tareas, empresas)
```

---

## Deploy (Cloudflare Pages)
- **Método:** `npx wrangler pages deploy . --project-name=clubcontable-web`
- **Dominio vinculado:** clubcontable.com (desde Cloudflare Pages → Custom domains)
- **Nota:** Antes del deploy quitar dominio con API, deployar, re-asignar

---

## Próximos pasos pendientes
- [ ] Verificar que **clubcontable.com** carga correctamente
- [ ] Confirmar SSL activo
- [ ] Configurar correos en Migadu (si se necesitan)
- [ ] Agregar SPF y DMARC en DNS de Cloudflare
- [ ] Subir a GitHub (sandluc22/club-contable)

---

## Google Search Console (pendiente)
- [ ] Verificar dominio en Google Search Console
- [ ] Enviar sitemap (cuando se genere)
