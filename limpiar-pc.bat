@echo off
echo ========================================
echo   LIMPIEZA RAPIDA PARA TU ORDENADOR
echo ========================================
echo.

echo [1/3] Borrando archivos temporales...
del /f /s /q "%TEMP%\*.*" >nul 2>&1
del /f /s /q "C:\Windows\Temp\*.*" >nul 2>&1
echo   Hecho!

echo [2/3] Vaciando papelera...
rd /s /q C:\$Recycle.bin >nul 2>&1
echo   Hecho!

echo [3/3] Limpiando DNS...
ipconfig /flushdns >nul
echo   Hecho!

echo.
echo ========================================
echo   LISTO! Ahora apaga y enciende el PC.
echo ========================================
pause
