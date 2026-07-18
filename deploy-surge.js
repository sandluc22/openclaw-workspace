const { spawn } = require('child_process');
const path = require('path');
const projectDir = path.resolve('/home/node/workspace/sandra-galilea');

const surge = spawn('npx', ['surge'], {
  cwd: projectDir,
  stdio: ['pipe', 'inherit', 'inherit'],
  env: { ...process.env, HOME: process.env.HOME }
});

// Give surge a moment to start, then send inputs
setTimeout(() => {
  surge.stdin.write('crecimientofinancieroglobal@gmail.com\n');
  setTimeout(() => {
    surge.stdin.write('Galilea2024!\n');
    setTimeout(() => {
      // Accept default project path
      surge.stdin.write('\n');
      setTimeout(() => {
        // Accept default domain suggestion
        surge.stdin.write('\n');
      }, 1000);
    }, 1000);
  }, 1000);
}, 2000);

surge.on('close', (code) => {
  console.log(`\n=== Exit code: ${code} ===`);
  process.exit(code || 0);
});

setTimeout(() => {
  console.log('\n=== TIMEOUT ===');
  surge.kill();
  process.exit(1);
}, 30000);
