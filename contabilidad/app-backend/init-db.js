// init-db.js - Inicializa la base de datos con tablas y datos de ejemplo
const initSqlJs = require('sql.js');
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcryptjs');

const DB_PATH = path.join(__dirname, 'data', 'contabilidad.db');

async function init() {
  const SQL = await initSqlJs();
  let db;
  const exists = fs.existsSync(DB_PATH);
  
  if (exists) {
    const buffer = fs.readFileSync(DB_PATH);
    db = new SQL.Database(buffer);
  } else {
    db = new SQL.Database();
  }

  // Ejecutar schema
  db.run(`
    CREATE TABLE IF NOT EXISTS usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL,
      rol TEXT NOT NULL DEFAULT 'responsable',
      activo INTEGER DEFAULT 1,
      created_at TEXT DEFAULT (datetime('now', '-5 hours'))
    );
    
    CREATE TABLE IF NOT EXISTS tareas (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      fecha TEXT NOT NULL,
      responsable TEXT DEFAULT '',
      tipo TEXT DEFAULT 'normal',
      notas TEXT DEFAULT '',
      completada INTEGER DEFAULT 0,
      completada_por INTEGER,
      completada_at TEXT,
      created_by INTEGER,
      created_at TEXT DEFAULT (datetime('now', '-5 hours')),
      updated_at TEXT DEFAULT (datetime('now', '-5 hours'))
    );
    
    CREATE TABLE IF NOT EXISTS auditoria (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      tarea_id INTEGER,
      usuario_id INTEGER,
      accion TEXT NOT NULL,
      detalle TEXT,
      created_at TEXT DEFAULT (datetime('now', '-5 hours'))
    );
  `);

  // Crear admin por defecto si no existe
  const adminExists = db.exec("SELECT id FROM usuarios WHERE email = 'admin@contabilidad.co'");
  if (adminExists.length === 0 || adminExists[0].values.length === 0) {
    const hash = bcrypt.hashSync('admin123', 10);
    db.run("INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)",
      ['Admin', 'admin@contabilidad.co', hash, 'admin']);
    console.log('✅ Admin creado: admin@contabilidad.co / admin123');
  }

  // Cargar datos por defecto solo si la tabla de tareas está vacía
  const tareasCount = db.exec("SELECT COUNT(*) as c FROM tareas");
  if (tareasCount[0].values[0][0] === 0) {
    const tareasDefault = [
      // Cierres contables mensuales
      { t: '📆 Cierre contable - Enero', f: '2026-02-05' },
      { t: '📆 Cierre contable - Febrero', f: '2026-03-05' },
      { t: '📆 Cierre contable - Marzo', f: '2026-04-05' },
      { t: '📆 Cierre contable - Abril', f: '2026-05-05' },
      { t: '📆 Cierre contable - Mayo', f: '2026-06-05' },
      { t: '📆 Cierre contable - Junio', f: '2026-07-05' },
      { t: '📆 Cierre contable - Julio', f: '2026-08-05' },
      { t: '📆 Cierre contable - Agosto', f: '2026-09-05' },
      { t: '📆 Cierre contable - Septiembre', f: '2026-10-05' },
      { t: '📆 Cierre contable - Octubre', f: '2026-11-05' },
      { t: '📆 Cierre contable - Noviembre', f: '2026-12-05' },
      { t: '📆 Cierre contable - Diciembre', f: '2027-01-10' },
      // IVA Bimestral
      { t: '💰 IVA Bimestral 1 (Ene-Feb)', f: '2026-03-10', tp: 'urgente' },
      { t: '💰 IVA Bimestral 2 (Mar-Abr)', f: '2026-05-10', tp: 'urgente' },
      { t: '💰 IVA Bimestral 3 (May-Jun)', f: '2026-07-10', tp: 'urgente' },
      { t: '💰 IVA Bimestral 4 (Jul-Ago)', f: '2026-09-10', tp: 'urgente' },
      { t: '💰 IVA Bimestral 5 (Sep-Oct)', f: '2026-11-10', tp: 'urgente' },
      { t: '💰 IVA Bimestral 6 (Nov-Dic)', f: '2027-01-10', tp: 'urgente' },
      // ReteFuente
      { t: '📄 ReteFuente - Febrero', f: '2026-03-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Marzo', f: '2026-04-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Abril', f: '2026-05-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Mayo', f: '2026-06-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Junio', f: '2026-07-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Julio', f: '2026-08-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Agosto', f: '2026-09-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Septiembre', f: '2026-10-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Octubre', f: '2026-11-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Noviembre', f: '2026-12-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Diciembre', f: '2027-01-10', tp: 'urgente' },
      { t: '📄 ReteFuente - Enero', f: '2026-02-10', tp: 'urgente' },
      // Otros
      { t: '📊 Declaración de Renta - Preparación', f: '2026-06-01' },
      { t: '📊 Declaración de Renta - Plazo máximo', f: '2026-08-15', tp: 'urgente', n: 'Plazo varía según último dígito NIT' },
      { t: '👥 Seguridad Social - Julio', f: '2026-07-05', tp: 'urgente' },
      { t: '👥 Seguridad Social - Agosto', f: '2026-08-05', tp: 'urgente' },
      { t: '👥 Seguridad Social - Septiembre', f: '2026-09-05', tp: 'urgente' },
      { t: '👥 Seguridad Social - Octubre', f: '2026-10-05', tp: 'urgente' },
      { t: '👥 Seguridad Social - Noviembre', f: '2026-11-05', tp: 'urgente' },
      { t: '👥 Seguridad Social - Diciembre', f: '2026-12-05', tp: 'urgente' },
      { t: '📋 Información Exógena DIAN', f: '2026-03-31', tp: 'urgente' },
      { t: '🎯 Cierre fiscal anual', f: '2027-01-15' },
      { t: '📑 Estados Financieros - Corte', f: '2026-12-31' },
      { t: '📑 Estados Financieros - Presentación', f: '2027-03-31', tp: 'urgente' },
    ];

    const stmt = db.prepare("INSERT INTO tareas (titulo, fecha, tipo, notas) VALUES (?, ?, ?, ?)");
    for (const t of tareasDefault) {
      stmt.run([t.t, t.f, t.tp || 'normal', t.n || '']);
    }
    stmt.free();
    console.log(`✅ ${tareasDefault.length} tareas por defecto insertadas`);
  }

  // Guardar
  const data = db.export();
  const buffer = Buffer.from(data);
  if (!exists) {
    fs.writeFileSync(DB_PATH, buffer);
  } else {
    // Escritura atómica
    const tmpPath = DB_PATH + '.tmp';
    fs.writeFileSync(tmpPath, buffer);
    fs.renameSync(tmpPath, DB_PATH);
  }
  db.close();
  console.log('✅ Base de datos inicializada:', DB_PATH);
}

init().catch(e => { console.error('Error:', e); process.exit(1); });
