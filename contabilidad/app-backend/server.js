// server.js - Servidor completo con auth, tareas y auditoría (sql.js fix)
const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const initSqlJs = require('sql.js');

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = 'cfg-co-secret-2026';
const DB_PATH = path.join(__dirname, 'data', 'contabilidad.db');

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Helpers BD
async function getDb() {
  const SQL = await initSqlJs();
  const buffer = fs.readFileSync(DB_PATH);
  return new SQL.Database(buffer);
}

function saveDb(db) {
  const data = db.export();
  const tmpPath = DB_PATH + '.tmp';
  fs.writeFileSync(tmpPath, Buffer.from(data));
  fs.renameSync(tmpPath, DB_PATH);
}

// Ejecutar query con bind (sql.js)
function dbExec(db, sql, params) {
  const stmt = db.prepare(sql);
  if (params && params.length > 0) {
    try { stmt.bind(params); } catch(e) {}
  }
  const rows = [];
  while (stmt.step()) rows.push(stmt.getAsObject());
  stmt.free();
  return rows;
}

function dbRun(db, sql, params) {
  db.run(sql, params);
}

// Auth middleware
function authMiddleware(req, res, next) {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (!token) return res.status(401).json({ error: 'Token requerido' });
  try {
    req.user = jwt.verify(token, JWT_SECRET);
    next();
  } catch (e) {
    return res.status(401).json({ error: 'Token inválido' });
  }
}

function adminMiddleware(req, res, next) {
  if (req.user.rol !== 'admin') return res.status(403).json({ error: 'Se requiere rol admin' });
  next();
}

// ============== RUTAS ==============

// POST /api/login (implementación directa sin dbExec por compatibilidad sql.js)
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) return res.status(400).json({ error: 'Email y contraseña requeridos' });
    const db = await getDb();
    const stmt = db.prepare("SELECT id, nombre, email, password, rol FROM usuarios WHERE email = ? AND activo = 1");
    stmt.bind([email]);
    const rows = [];
    while (stmt.step()) rows.push(stmt.getAsObject());
    stmt.free();
    db.close();
    if (rows.length === 0) return res.status(401).json({ error: 'Credenciales inválidas' });
    const user = rows[0];
    if (!bcrypt.compareSync(password, user.password)) return res.status(401).json({ error: 'Credenciales inválidas' });
    const token = jwt.sign({ id: user.id, nombre: user.nombre, email: user.email, rol: user.rol }, JWT_SECRET, { expiresIn: '30d' });
    res.json({ token, usuario: { id: user.id, nombre: user.nombre, email: user.email, rol: user.rol } });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// GET /api/perfil
app.get('/api/perfil', authMiddleware, (req, res) => {
  res.json({ usuario: req.user });
});

// GET /api/usuarios (admin)
app.get('/api/usuarios', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    const rows = dbExec(db, "SELECT id, nombre, email, rol, activo, created_at FROM usuarios ORDER BY nombre");
    db.close();
    res.json(rows);
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// POST /api/usuarios (admin)
app.post('/api/usuarios', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const { nombre, email, password, rol } = req.body;
    if (!nombre || !email || !password) return res.status(400).json({ error: 'Campos obligatorios' });
    const hash = bcrypt.hashSync(password, 10);
    const db = await getDb();
    dbRun(db, "INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)", [nombre, email, hash, rol || 'responsable']);
    saveDb(db);
    db.close();
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// PUT /api/usuarios/:id (admin)
app.put('/api/usuarios/:id', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const { nombre, email, password, rol, activo } = req.body;
    const db = await getDb();
    if (password) {
      const hash = bcrypt.hashSync(password, 10);
      dbRun(db, "UPDATE usuarios SET nombre=?, email=?, password=?, rol=?, activo=? WHERE id=?", [nombre, email, hash, rol, activo ?? 1, req.params.id]);
    } else {
      dbRun(db, "UPDATE usuarios SET nombre=?, email=?, rol=?, activo=? WHERE id=?", [nombre, email, rol, activo ?? 1, req.params.id]);
    }
    saveDb(db);
    db.close();
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// DELETE /api/usuarios/:id (admin)
app.delete('/api/usuarios/:id', authMiddleware, adminMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    dbRun(db, "DELETE FROM usuarios WHERE id = ?", [req.params.id]);
    saveDb(db);
    db.close();
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// GET /api/tareas
app.get('/api/tareas', authMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    const rows = dbExec(db, "SELECT id, titulo, fecha, responsable, tipo, notas, completada, completada_por, completada_at, created_by, created_at, updated_at FROM tareas ORDER BY fecha ASC");
    db.close();
    rows.forEach(r => r.completada = !!r.completada);
    res.json(rows);
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// POST /api/tareas
app.post('/api/tareas', authMiddleware, async (req, res) => {
  try {
    const { titulo, fecha, responsable, tipo, notas } = req.body;
    if (!titulo || !fecha) return res.status(400).json({ error: 'Título y fecha obligatorios' });
    const db = await getDb();
    dbRun(db, "INSERT INTO tareas (titulo, fecha, responsable, tipo, notas, created_by) VALUES (?, ?, ?, ?, ?, ?)",
      [titulo, fecha, responsable || '', tipo || 'normal', notas || '', req.user.id]);
    const rows = dbExec(db, "SELECT MAX(id) as id FROM tareas");
    const newId = rows[0].id;
    dbRun(db, "INSERT INTO auditoria (tarea_id, usuario_id, accion, detalle) VALUES (?, ?, 'creada', ?)",
      [newId, req.user.id, `${req.user.nombre} creó: ${titulo}`]);
    saveDb(db);
    db.close();
    res.json({ ok: true, id: newId });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// PUT /api/tareas/:id
app.put('/api/tareas/:id', authMiddleware, async (req, res) => {
  try {
    const { titulo, fecha, responsable, tipo, notas } = req.body;
    const db = await getDb();
    dbRun(db, "UPDATE tareas SET titulo=?, fecha=?, responsable=?, tipo=?, notas=?, updated_at=datetime('now', '-5 hours') WHERE id=?",
      [titulo, fecha, responsable || '', tipo || 'normal', notas || '', req.params.id]);
    dbRun(db, "INSERT INTO auditoria (tarea_id, usuario_id, accion, detalle) VALUES (?, ?, 'editada', ?)",
      [req.params.id, req.user.id, `${req.user.nombre} editó: ${titulo}`]);
    saveDb(db);
    db.close();
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// PUT /api/tareas/:id/toggle
app.put('/api/tareas/:id/toggle', authMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    const rows = dbExec(db, "SELECT id, titulo, completada FROM tareas WHERE id = ?", [req.params.id]);
    if (rows.length === 0) { db.close(); return res.status(404).json({ error: 'No encontrada' }); }
    const t = rows[0];
    const nueva = t.completada ? 0 : 1;
    if (nueva) {
      dbRun(db, "UPDATE tareas SET completada=1, completada_por=?, completada_at=datetime('now', '-5 hours') WHERE id=?", [req.user.id, t.id]);
    } else {
      dbRun(db, "UPDATE tareas SET completada=0, completada_por=NULL, completada_at=NULL WHERE id=?", [t.id]);
    }
    const detalle = nueva ? `${req.user.nombre} completó: ${t.titulo}` : `${req.user.nombre} reabrió: ${t.titulo}`;
    const accion = nueva ? 'completada' : 'reabierta';
    dbRun(db, "INSERT INTO auditoria (tarea_id, usuario_id, accion, detalle) VALUES (?, ?, ?, ?)", [t.id, req.user.id, accion, detalle]);
    saveDb(db);
    db.close();
    res.json({ ok: true, completada: !!nueva });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// DELETE /api/tareas/:id
app.delete('/api/tareas/:id', authMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    const rows = dbExec(db, "SELECT titulo FROM tareas WHERE id = ?", [req.params.id]);
    const titulo = rows[0]?.titulo || '';
    dbRun(db, "DELETE FROM tareas WHERE id = ?", [req.params.id]);
    dbRun(db, "INSERT INTO auditoria (tarea_id, usuario_id, accion, detalle) VALUES (?, ?, 'eliminada', ?)",
      [req.params.id, req.user.id, `${req.user.nombre} eliminó: ${titulo}`]);
    saveDb(db);
    db.close();
    res.json({ ok: true });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// GET /api/auditoria
app.get('/api/auditoria', authMiddleware, async (req, res) => {
  try {
    const db = await getDb();
    const rows = dbExec(db,
      "SELECT a.id, a.tarea_id, a.usuario_id, u.nombre as usuario_nombre, a.accion, a.detalle, a.created_at FROM auditoria a LEFT JOIN usuarios u ON a.usuario_id = u.id ORDER BY a.created_at DESC LIMIT 200");
    db.close();
    res.json(rows);
  } catch (e) { res.status(500).json({ error: e.message }); }
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
  console.log(`✅ Servidor contable Colombia corriendo en puerto ${PORT}`);
});
