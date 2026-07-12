# 🏢 Club Contable — Pendiente para retomar

## ✅ COMPLETADO (11 julio)

- [x] **Login por usuario** — 4 usuarios creados: Sandra (admin), María Ángel, Yurleny, Kareling
- [x] **Reorganización de categorías**: Impuestos (IVA, Retefuente, Renta, Exógena, RUB, Reteica), Laboral (Seg. Social, Nómina), Contabilidad (Compras, Tesorería, Activos Fijos, Financiero, Facturación), Reporte Entidades (RNB, Supersociedades, Plan Maestro, Cámara Comercio, Otra), Visitas (Revisoría, Aud. Régimen Franco, Aud. Sagrilatf, Otra), Solicitud Áreas (Accionistas, Gerencia Gral, Gerencia Admin/Fin, Operaciones, Of. Cumplimiento, Otra)
- [x] **Nameservers cambiados** en Namecheap a Netlify (dns1.p01.nsone.net)
- [x] **HTML actualizado y guardado** en clubcontable/codigo/index.html
- [x] **Backups guardados** (.bak, .bak2, .bak_antes_categorias)

## 🚧 PENDIENTE (próximos pasos)

### Prioridad: que cargue el dominio
- [ ] **Esperar propagación DNS** (hasta 24h desde el cambio en Namecheap)
- [ ] **Confirmar SSL automático** de Netlify para clubcontable.com
- [ ] **Verificar que clubcontable.com carga** con login y nuevas categorías

### Después de que cargue
- [ ] **Añadir tareas a categorías nuevas**: Reporte Entidades, Visitas, Solicitud Áreas y subcategorías vacías
- [ ] **Asignar tareas por usuario** — que cada usuario vea solo sus tareas
- [ ] **Marcar tareas como completadas** y que se guarde el estado
- [ ] **Correo semanal (lunes):** enviar resumen de tareas pendientes a cada responsable
- [ ] **Tareas recurrentes:** que se repitan cada mes automáticamente
- [ ] **Tareas extra:** poder añadir tareas solo para un mes concreto
- [ ] **Fecha de entrega:** cada tarea con su fecha límite
- [ ] **Migración futura a backend** con base de datos (cuando crezca)

## 🔑 Credenciales de acceso

| Usuario | Contraseña | Rol |
|---|---|---|
| Sandra | Sandra2026 | Administradora |
| María Ángel | Maria2026 | Usuario |
| Yurleny | Yurleny2026 | Usuario |
| Kareling | Kareling2026 | Usuario |

## 📁 Archivos
- HTML: `clubcontable/codigo/index.html`
- Backups: `.bak`, `.bak2`, `.bak_antes_categorias`

## 🎯 OBJETIVO FINAL
> **Vender Club Contable como servicio por suscripción mensual** a contadores, asesores y pequeños negocios. Cada contador con su panel de clientes, ingresos recurrentes.

## Notas
- El HTML actual tiene los datos en localStorage → toca migrar a backend cuando haya más usuarios
- Las 67 tareas existentes se han recategorizado a la nueva estructura
