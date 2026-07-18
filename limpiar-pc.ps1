Write-Host "========================================" -ForegroundColor Yellow
Write-Host "  LIMPIEZA RÁPIDA - Windows LENTO" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
Write-Host ""

# 1. Borrar archivos temporales
Write-Host "[1/5] Eliminando archivos temporales..." -ForegroundColor Cyan
$tempFolders = @("$env:TEMP", "$env:WINDIR\Temp", "$env:WINDIR\Prefetch")
foreach ($folder in $tempFolders) {
    if (Test-Path $folder) {
        try {
            Get-ChildItem -Path $folder -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
            Write-Host "  ✓ Limpiado: $folder" -ForegroundColor Green
        } catch {
            Write-Host "  - Omitido (en uso): $folder" -ForegroundColor Gray
        }
    }
}

# 2. Vaciar papelera
Write-Host "[2/5] Vaciando papelera de reciclaje..." -ForegroundColor Cyan
try {
    (New-Object -ComObject Shell.Application).NameSpace(0xa).Items() | ForEach-Object { $_.InvokeVerb("delete") }
    Write-Host "  ✓ Papelera vaciada" -ForegroundColor Green
} catch {
    Write-Host "  - No se pudo vaciar papelera automáticamente" -ForegroundColor Gray
}

# 3. Deshabilitar servicios de Dell (basura)
Write-Host "[3/5] Deshabilitando Dell Instrumentation..." -ForegroundColor Cyan
$dellServices = Get-Service -Name "*Dell*" -ErrorAction SilentlyContinue
if ($dellServices) {
    foreach ($svc in $dellServices) {
        try {
            Stop-Service $svc.Name -Force -ErrorAction SilentlyContinue
            Set-Service $svc.Name -StartupType Disabled -ErrorAction SilentlyContinue
            Write-Host "  ✓ Deshabilitado: $($svc.Name)" -ForegroundColor Green
        } catch {
            Write-Host "  - Error con: $($svc.Name)" -ForegroundColor Gray
        }
    }
} else {
    Write-Host "  - No se encontraron servicios Dell" -ForegroundColor Gray
}

# 4. Limpiar archivos de Windows Update
Write-Host "[4/5] Limpiando caché de Windows Update..." -ForegroundColor Cyan
try {
    Stop-Service wuauserv -Force -ErrorAction SilentlyContinue
    Stop-Service bits -Force -ErrorAction SilentlyContinue
    $updateCache = "$env:WINDIR\SoftwareDistribution\Download"
    if (Test-Path $updateCache) {
        Get-ChildItem -Path $updateCache -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
        Write-Host "  ✓ Caché de actualizaciones limpiada" -ForegroundColor Green
    }
    Start-Service wuauserv -ErrorAction SilentlyContinue
    Start-Service bits -ErrorAction SilentlyContinue
} catch {
    Write-Host "  - Error al limpiar caché de actualizaciones" -ForegroundColor Gray
}

# 5. Limpiar DNS
Write-Host "[5/5] Limpiando DNS..." -ForegroundColor Cyan
try {
    ipconfig /flushdns | Out-Null
    Write-Host "  ✓ DNS limpiado" -ForegroundColor Green
} catch {
    Write-Host "  - Error al limpiar DNS" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "  ✅ LISTO. Cierra y abre el ordenador." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Yellow
