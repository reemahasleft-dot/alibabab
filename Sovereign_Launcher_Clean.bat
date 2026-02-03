@echo off
chcp 65001 >nul
title SOVEREIGN SYSTEM 2026
color 0A

echo.
echo   ================================================
echo          SOVEREIGN UNIFIED SYSTEM 2026
echo   ================================================
echo.
echo   Architect: Ali Essa
echo   Date: %date% %time%
echo.

:menu
echo.
echo [1] CORE SYSTEM (Monitoring & Dashboard)
echo [2] LIVE DASHBOARD (Open in Browser)
echo [3] AI ASSISTANT (Ollama)
echo [4] GAME OPTIMIZER
echo [5] SECURITY SYSTEM
echo [6] ARCHITECTURAL TOOLS
echo [7] DIAGNOSTIC AI
echo [8] WISDOM BASE
echo [9] COMPLETE SYSTEM
echo [0] STOP ALL SYSTEMS
echo [X] EXIT
echo.

set /p choice=Enter choice (1-9, 0, X): 

if "%choice%"=="1" (
    echo Starting Core System...
    python sovereign_core_v5_enhanced.py
    goto menu
)

if "%choice%"=="2" (
    echo Opening Live Dashboard...
    start "" "Dashboard\sovereign_dashboard_LIVE.html"
    goto menu
)

if "%choice%"=="3" (
    echo Starting AI Assistant...
    python Sovereign_Real_AI.py
    goto menu
)

if "%choice%"=="4" (
    echo Starting Game Optimizer...
    python Sovereign_Proactive_Engine.py
    goto menu
)

if "%choice%"=="5" (
    echo Starting Security System...
    python Sovereign_Shield.py
    goto menu
)

if "%choice%"=="6" (
    echo Starting Architectural Tools...
    python Sovereign_Parametric_Core.py
    goto menu
)

if "%choice%"=="7" (
    echo Starting Diagnostic AI...
    python Sovereign_Diagnostic_AI.py
    goto menu
)

if "%choice%"=="8" (
    echo Opening Wisdom Base...
    notepad "Sovereign_Wisdom_2026_Pro.txt"
    goto menu
)

if "%choice%"=="9" (
    echo Starting Complete System...
    python Sovereign_Complete_System.py
    goto menu
)

if "%choice%"=="0" (
    echo Stopping all systems...
    taskkill /f /im python.exe 2>nul
    echo All systems stopped.
    timeout /t 2 >nul
    goto menu
)

if /i "%choice%"=="X" (
    exit /b 0
)

echo Invalid choice.
timeout /t 2 >nul
goto menu