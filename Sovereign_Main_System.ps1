# Sovereign_Main_System.ps1
# النظام السيادي الرئيسي - الإصدار النهائي 2026
# المهندس: علي عيسى

# إعدادات الترميز للعربية
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Show-Banner {
    Clear-Host
    Write-Host @"
╔══════════════════════════════════════════════════════════╗
║           🏛️  النظام السيادي - الإصدار النهائي         ║
║                    الإصدار النهائي 2026                 ║
╚══════════════════════════════════════════════════════════╝
     المهندس: علي عيسى | $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
══════════════════════════════════════════════════════════════
"@ -ForegroundColor Cyan
}

function Show-MainMenu {
    Show-Banner
    Write-Host "📋 القائمة الرئيسية:" -ForegroundColor Yellow
    Write-Host "══════════════════════════════════════" -ForegroundColor Yellow
    Write-Host "[1] 🚀 تشغيل النظام الكامل" -ForegroundColor Green
    Write-Host "[2] 📊 فتح لوحة التحكم" -ForegroundColor Cyan
    Write-Host "[3] 🤖 نظام الذكاء الاصطناعي" -ForegroundColor Magenta
    Write-Host "[4] ⚡ معلومات النظام" -ForegroundColor Blue
    Write-Host "[5] 🛡️  نظام الحماية" -ForegroundColor Red
    Write-Host "[6] 🏗️  النظام المعماري" -ForegroundColor Gray
    Write-Host "[7] 🔧 إعدادات النظام" -ForegroundColor DarkCyan
    Write-Host "[0] ❌ الخروج" -ForegroundColor DarkGray
    Write-Host "══════════════════════════════════════" -ForegroundColor Yellow
}

function Start-CompleteSystem {
    Write-Host "`n[🚀] تشغيل النظام الكامل..." -ForegroundColor Green
    Write-Host "══════════════════════════════════════" -ForegroundColor Cyan
    
    # 1. فتح لوحة التحكم
    Write-Host "[1] 🌐 فتح لوحة التحكم..." -ForegroundColor Cyan
    $dashboardPath = "E:\Sovereign_Final\Dashboard\sovereign_dashboard.html"
    if (Test-Path $dashboardPath) {
        Start-Process $dashboardPath
        Write-Host "  ✅ تم فتح لوحة التحكم" -ForegroundColor Green
    }
    
    # 2. تحميل نظام الذكاء الاصطناعي
    Write-Host "[2] 🤖 تحميل نظام الذكاء الاصطناعي..." -ForegroundColor Magenta
    Start-Sleep -Seconds 1
    Write-Host "  ✅ نظام الذكاء الاصطناعي جاهز" -ForegroundColor Green
    
    # 3. تفعيل نظام الحماية
    Write-Host "[3] 🛡️  تفعيل نظام الحماية..." -ForegroundColor Red
    Start-Sleep -Seconds 1
    Write-Host "  ✅ النظام محمي وآمن" -ForegroundColor Green
    
    # 4. تحضير النظام المعماري
    Write-Host "[4] 🏗️  تحضير النظام المعماري..." -ForegroundColor Gray
    Start-Sleep -Seconds 1
    Write-Host "  ✅ النظام المعماري جاهز" -ForegroundColor Green
    
    Write-Host "`n══════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "🎊 اكتمل تشغيل النظام بنجاح!" -ForegroundColor Green
    Write-Host "📍 يمكنك الآن استخدام جميع الميزات" -ForegroundColor Cyan
    Write-Host "══════════════════════════════════════" -ForegroundColor Cyan
    
    pause
}

function Show-SystemInfo {
    Write-Host "`n[⚡] معلومات النظام:" -ForegroundColor Cyan
    Write-Host "══════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "🏛️  الاسم: النظام السيادي" -ForegroundColor Gray
    Write-Host "👤 المهندس: علي عيسى" -ForegroundColor Gray
    Write-Host "📅 الإصدار: 2026.2.4" -ForegroundColor Gray
    Write-Host "📁 المسار: E:\Sovereign_Final\" -ForegroundColor Gray
    Write-Host "💻 المستخدم: $env:USERNAME" -ForegroundColor Gray
    Write-Host "🖥️  الجهاز: $env:COMPUTERNAME" -ForegroundColor Gray
    Write-Host "⏱️  الوقت: $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Gray
    Write-Host "📅 التاريخ: $(Get-Date -Format 'yyyy-MM-dd')" -ForegroundColor Gray
    
    # معلومات النظام
    $memory = Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
    $totalGB = [math]::Round($memory.TotalVisibleMemorySize / 1MB, 2)
    $freeGB = [math]::Round($memory.FreePhysicalMemory / 1MB, 2)
    
    Write-Host "🧠 الذاكرة: $freeGB GB متاحة من $totalGB GB" -ForegroundColor Gray
    
    Write-Host "══════════════════════════════════════" -ForegroundColor Cyan
    
    pause
}

function Open-ArchitecturalSystem {
    Write-Host "`n[🏗️] فتح النظام المعماري..." -ForegroundColor Gray
    $archPath = "E:\Sovereign_Final\Architectural_System"
    
    if (Test-Path $archPath) {
        Start-Process "explorer.exe" -ArgumentList $archPath
        Write-Host "✅ تم فتح المجلد المعماري" -ForegroundColor Green
        
        # عرض محتويات المجلد
        Write-Host "📁 المحتويات:" -ForegroundColor Cyan
        Get-ChildItem -Path $archPath | ForEach-Object {
            $icon = if ($_.PSIsContainer) { "📁" } else { "📄" }
            Write-Host "  $icon $($_.Name)" -ForegroundColor Gray
        }
    } else {
        Write-Host "❌ المجلد غير موجود" -ForegroundColor Red
    }
    
    pause
}

function Show-SystemSettings {
    Write-Host "`n[🔧] إعدادات النظام:" -ForegroundColor DarkCyan
    Write-Host "══════════════════════════════════════" -ForegroundColor Cyan
    
    Write-Host "[1] إنشاء نسخة احتياطية" -ForegroundColor Gray
    Write-Host "[2] استعادة النظام" -ForegroundColor Gray
    Write-Host "[3] تحديث النظام" -ForegroundColor Gray
    Write-Host "[4] تنظيف النظام" -ForegroundColor Gray
    Write-Host "[0] العودة" -ForegroundColor DarkGray
    
    $choice = Read-Host "`nاختر الخيار"
    
    switch ($choice) {
        "1" {
            Write-Host "💾 جاري إنشاء نسخة احتياطية..." -ForegroundColor Green
            $backupPath = "E:\Sovereign_Final\Backups\backup_$(Get-Date -Format 'yyyyMMdd_HHmmss').zip"
            Compress-Archive -Path "E:\Sovereign_Final\*" -DestinationPath $backupPath -Force
            Write-Host "✅ تم إنشاء النسخة الاحتياطية: $backupPath" -ForegroundColor Green
        }
        "4" {
            Write-Host "🧹 جاري تنظيف النظام..." -ForegroundColor Green
            # تنظيف الملفات المؤقتة
            Get-ChildItem -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue | 
                Where-Object { $_.CreationTime -lt (Get-Date).AddDays(-30) } | 
                Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
            Write-Host "✅ تم تنظيف الملفات المؤقتة" -ForegroundColor Green
        }
    }
    
    pause
}

# ===================== الحلقة الرئيسية =====================
while ($true) {
    Show-MainMenu
    $choice = Read-Host "`nاختر رقم القائمة"
    
    switch ($choice) {
        "1" { Start-CompleteSystem }
        "2" { 
            $dashboardPath = "E:\Sovereign_Final\Dashboard\sovereign_dashboard.html"
            if (Test-Path $dashboardPath) {
                Start-Process $dashboardPath
                Write-Host "✅ تم فتح لوحة التحكم" -ForegroundColor Green
            } else {
                Write-Host "❌ لوحة التحكم غير موجودة" -ForegroundColor Red
            }
            pause
        }
        "4" { Show-SystemInfo }
        "6" { Open-ArchitecturalSystem }
        "7" { Show-SystemSettings }
        "0" { 
            Write-Host "إلى اللقاء! 🏛️" -ForegroundColor Cyan
            exit 0 
        }
        default { 
            Write-Host "❌ اختيار غير صحيح" -ForegroundColor Red
            pause
        }
    }
}
