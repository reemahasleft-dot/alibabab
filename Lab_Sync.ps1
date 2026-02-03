Write-Host ">>> OPENING LINUX GATEWAY (UBUNTU)..." -ForegroundColor Cyan
wsl -d Ubuntu true # إيقاظ اللينكس برمجياً

# تعريف المسارات بناءً على هندسة جهازك
$src = "\\wsl.localhost\Ubuntu\home\ali_essa\projects"
$dst = "E:\Sovereign_Archives\Source_Code\Sync_2026-02-02_00-25"

if (Test-Path $src) {
    Write-Host ">>> BREACHING LAB DATA..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $dst -Force
    # استخدام Robocopy لسرعة الـ Samsung 9100 PRO
    robocopy $src $dst /MIR /MT:32 /R:2 /W:5
    Write-Host ">>> DATA ARCHIVED SUCCESSFULLY TO DISK E." -ForegroundColor Green
} else {
    Write-Host ">>> ERROR: LAB PATH NOT ACCESSIBLE. CHECK WSL STATUS." -ForegroundColor Red
}
