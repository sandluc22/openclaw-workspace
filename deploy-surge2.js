const { spawn } = require('child_process');
const path = require('path');
const projectDir = '/home/node/workspace/sandra-galilea';

const surge = spawn('npx', ['surge', '--domain', 'crecimientofinancieroglobal.surge.sh'], {
  cwd: projectDir,
  stdio: ['pipe', 'inherit', 'inherit'],
  env: { ...process.env, HOME: process.env.HOME }
});

// Already logged in, just need to confirm project+domain
setTimeout(() => {
  surge.stdin.write(projectDir + '\n');
}, 1000);

setTimeout(() => {
  surge.stdin.write('crecimientofinancieroglobal.surge.sh\n');
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
