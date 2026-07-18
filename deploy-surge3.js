const { spawn } = require('child_process');
const surge = spawn('npx', ['surge', '--domain', 'crecimientofinancieroglobal.surge.sh'], {
  cwd: '/home/node/workspace/sandra-galilea',
  stdio: ['pipe', 'inherit', 'inherit'],
  env: { ...process.env, HOME: process.env.HOME }
});

setTimeout(() => surge.stdin.write('/home/node/workspace/sandra-galilea\n'), 1000);
setTimeout(() => surge.stdin.write('crecimientofinancieroglobal.surge.sh\n'), 2000);

surge.on('close', (code) => { process.exit(code || 0); });
setTimeout(() => { console.log('\n=== TIMEOUT ==='); surge.kill(); process.exit(1); }, 30000);
