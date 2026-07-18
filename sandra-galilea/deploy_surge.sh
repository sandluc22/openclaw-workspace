#!/usr/bin/expect -f
set timeout 30
spawn npx surge --domain sandra-galilea.surge.sh
expect "email:"
send "crecimientofinancieroglobal@gmail.com\r"
expect "password:"
send "Galilea2026!\r"
expect eof
