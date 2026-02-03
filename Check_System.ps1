# 🛠️ ملف مراقبة النظام
Write-Host "🔍 مراقبة النظام السيادي..." -ForegroundColor Cyan

function Get-SystemHealth {
    $cpu = Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select-Object -ExpandProperty Average
    $ram = Get-WmiObject Win32_OperatingSystem | ForEach-Object { 
        [math]::Round((($_.TotalVisibleMemorySize - $_.FreePhysicalMemory) / $_.TotalVisibleMemorySize) * 100, 2)
    }
    
    return @{
        CPU = [math]::Round($cpu, 2)
        RAM = $ram
        Time = Get-Date -Format "HH:mm:ss"
    }
}

Write-Host "`n📊 حالة النظام:" -ForegroundColor Yellow
$health = Get-SystemHealth
Write-Host "• المعالج: $($health.CPU)%" -ForegroundColor White
Write-Host "• الذاكرة: $($health.RAM)%" -ForegroundColor White
Write-Host "• الوقت: $($health.Time)" -ForegroundColor White

Write-Host "`n📁 الملفات الأساسية:" -ForegroundColor Yellow
Get-ChildItem -Path $PWD -File | Select-Object -First 10 | ForEach-Object {
    Write-Host "• $($_.Name) ($([math]::Round($_.Length/1KB, 2)) KB)" -ForegroundColor White
}

Write-Host "`n✅ النظام جاهز للتشغيل" -ForegroundColor Green
Write-Host "🚀 للتشغيل: انقر على Start_Sovereign.bat" -ForegroundColor Cyan
