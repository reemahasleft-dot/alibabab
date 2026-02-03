Write-Host ">>> FLUSHING SYSTEM DNS CACHE..." -ForegroundColor Cyan
Clear-DnsClientCache

Write-Host ">>> CLEANING WATERFOX DEEP TRACKERS..." -ForegroundColor Yellow
$wf_path = "$env:APPDATA\Waterfox\Profiles"
if (Test-Path $wf_path) {
    # حذف ملفات الجلسات المؤقتة وسجلات البحث العميقة
    Get-ChildItem -Path $wf_path -Recurse -Include *.sqlite-wal, *.sqlite-shm, *.tmp | Remove-Item -Force -ErrorAction SilentlyContinue
    Write-Host ">>> WATERFOX PROFILE CLEANSED." -ForegroundColor Green
}

Write-Host ">>> BLOCKING WINDOWS TELEMETRY HOSTS..." -ForegroundColor Red
# إضافة عناوين تتبع مايكروسوفت إلى ملف الـ Hosts لمنعها من الاتصال
$hosts_path = "C:\Windows\System32\drivers\etc\hosts"
$tracking_domains = @("v10.events.data.microsoft.com", "v20.events.data.microsoft.com", "telemetry.microsoft.com")
foreach ($domain in $tracking_domains) {
    if (!(Select-String -Path $hosts_path -Pattern $domain)) {
        Add-Content -Path $hosts_path -Value "0.0.0.0 $domain"
    }
}
