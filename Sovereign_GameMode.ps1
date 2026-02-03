Write-Host ">>> INITIATING EMERGENCY PERFORMANCE PROTOCOL..." -ForegroundColor Red

# 1. تنظيف الذاكرة العشوائية فوراً
Write-Host ">>> PURGING STANDBY MEMORY..." -ForegroundColor Yellow
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

# 2. رفع أولوية الأداء العام للنظام
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c # High Performance

# 3. إيقاف الخدمات التي تسبب "Stuttering" أثناء اللعب
$Services = @("SysMain", "TabletInputService", "WSearch")
foreach ($Service in $Services) {
    if ((Get-Service $Service).Status -eq 'Running') {
        Stop-Service -Name $Service -Force
        Write-Host ">>> SERVICE $Service SUSPENDED FOR COMBAT." -ForegroundColor Gray
    }
}

Write-Host ">>> PERFORMANCE IS NOW LOCKED FOR GAMING DOMINANCE." -ForegroundColor Green
