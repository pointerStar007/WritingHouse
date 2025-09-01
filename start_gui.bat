@echo off
echo Starting WritingHouse GUI Launcher...
echo.

:: 检查是否存在已构建的exe文件
if exist "dist\WritingHouse-Launcher.exe" (
    echo Running executable version...
    start "" "dist\WritingHouse-Launcher.exe"
    exit /b 0
)

:: 如果没有exe文件，直接运行Python脚本
echo Running Python version...
python launcher_gui.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start GUI launcher
    echo Please ensure Python is installed and try again
    echo.
    echo To build executable version, run: build_launcher.bat
    echo.
    pause
)