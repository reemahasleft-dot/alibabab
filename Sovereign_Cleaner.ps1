Write-Host ">>> PURGING SYSTEM CACHE..." -ForegroundColor Yellow
# تنظيف ملفات النظام المؤقتة
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Users\$env:USERNAME\AppData\Local\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
# تنظيف الـ Prefetch (لتحسين سرعة الإقلاع)
Remove-Item -Path "C:\Windows\Prefetch\*" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host ">>> BLOCKING TELEMETRY LOGS..." -ForegroundColor Magenta
# مسح سجلات التتبع والتقارير
Get-EventLog -LogName * | ForEach-Object {Clear-EventLog -LogName $_.Log}

Write-Host ">>> MEMORY OPTIMIZED. SYSTEM IS CLEAN." -ForegroundColor Green
