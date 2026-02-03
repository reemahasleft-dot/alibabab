@echo off
chcp 1256 >nul 2>nul
chcp 65001 >nul
title 🏛️ النظام السيادي الكامل - الإصدار النهائي 2026
color 0A

echo.
echo   ╔══════════════════════════════════════════════════════╗
echo   ║          النظام السيادي - الإصدار النهائي 2026      ║
echo   ╚══════════════════════════════════════════════════════╝
echo.
echo   المهندس: علي عيسى
echo   التاريخ: %date%
echo.

set "SYSTEM_PATH=%~dp0"

:menu
echo.
echo قائمة الأنظمة المتاحة:
echo.
echo [1] النظام الأساسي (المراقبة والتحديث)
echo [2] لوحة التحكم الحية
echo [3] الذكاء الاصطناعي والمحاور
echo [4] محسن الألعاب والأداء
echo [5] الأمان والحماية
echo [6] الأنظمة المعمارية
echo [7] التشخيص الذاتي
echo [8] قاعدة الحكمة والمعرفة
echo [9] النظام الكامل (جميع الأنظمة)
echo [0] إيقاف جميع الأنظمة
echo [X] الخروج
echo.

set /p choice=اختر رقم النظام: 

if "%choice%"=="1" (
    echo تشغيل النظام الأساسي...
    python "%SYSTEM_PATH%sovereign_core_v5_enhanced.py"
    goto menu
)

if "%choice%"=="2" (
    echo فتح لوحة التحكم...
    start "" "%SYSTEM_PATH%Dashboard\sovereign_dashboard_LIVE.html"
    goto menu
)

if "%choice%"=="3" (
    echo تشغيل أنظمة الذكاء الاصطناعي...
    python "%SYSTEM_PATH%Sovereign_Real_AI.py"
    goto menu
)

if "%choice%"=="4" (
    echo تشغيل محسن الأداء...
    python "%SYSTEM_PATH%Sovereign_Proactive_Engine.py"
    goto menu
)

if "%choice%"=="5" (
    echo تشغيل أنظمة الأمان...
    python "%SYSTEM_PATH%Sovereign_Shield.py"
    goto menu
)

if "%choice%"=="6" (
    echo تشغيل الأنظمة المعمارية...
    python "%SYSTEM_PATH%Sovereign_Parametric_Core.py"
    goto menu
)

if "%choice%"=="7" (
    echo تشغيل التشخيص الذاتي...
    python "%SYSTEM_PATH%Sovereign_Diagnostic_AI.py"
    goto menu
)

if "%choice%"=="8" (
    echo فتح قاعدة الحكمة...
    notepad "%SYSTEM_PATH%Sovereign_Wisdom_2026_Pro.txt"
    goto menu
)

if "%choice%"=="9" (
    echo تشغيل النظام الكامل...
    python "%SYSTEM_PATH%Sovereign_Complete_System.py"
    goto menu
)

if "%choice%"=="0" (
    echo إيقاف جميع الأنظمة...
    taskkill /f /im python.exe 2>nul
    echo تم إيقاف جميع الأنظمة.
    timeout /t 2 >nul
    goto menu
)

if /i "%choice%"=="X" (
    exit /b 0
)

echo اختيار غير صالح.
timeout /t 2 >nul
goto menu
