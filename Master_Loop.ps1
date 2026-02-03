while ($true) {
    # تنظيف الذاكرة كل ساعة لضمان السرعة
    Clear-DnsClientCache
    # مزامنة هادئة
    powershell -File "D:\Sovereign_System\Lab_Sync.ps1"
    Start-Sleep -Seconds 3600
}

if ((Get-Date).DayOfWeek -eq 'Friday') { powershell -File "D:\Sovereign_System\Sovereign_Snapshot.ps1" }
