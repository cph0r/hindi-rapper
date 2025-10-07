@echo off
REM Hindi Rap Generator Launcher Script for Windows
REM This script sets up and launches the Hindi Rap Generator UI

echo.
echo 🎤 Hindi Rap Generator (हिंदी रैप जनरेटर)
echo ==========================================
echo.

REM Set Python path
set PYTHONPATH=%PYTHONPATH%;%CD%

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher
    pause
    exit /b 1
)

REM Check if gradio is installed
python -c "import gradio" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Installing Gradio...
    pip install gradio
)

REM Check CUDA availability
for /f "tokens=*" %%i in ('python -c "import torch; print('CUDA' if torch.cuda.is_available() else 'CPU')"') do set DEVICE=%%i
echo 🖥️  Running on: %DEVICE%

if "%DEVICE%"=="CPU" (
    echo ⚠️  Warning: No GPU detected. Generation will be slower.
)

echo.
echo 🚀 Starting Hindi Rap Generator UI...
echo 📱 Web interface will open at: http://localhost:7860
echo.
echo Press Ctrl+C to stop the server
echo ==========================================
echo.

REM Launch the UI
python hindi_rap_ui.py %*

pause

