@echo off
chcp 65001 >nul
color 0A
echo.
echo ========================================
echo          WritingHouse - Start Script
echo ========================================
echo.

:: Check Node.js
echo [1/4] Checking Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Node.js not found, please install Node.js first
    echo Download: https://nodejs.org/
    pause
    exit /b 1
)
echo Node.js OK

:: Check Python
echo [2/4] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found, please install Python first
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo Python OK

:: Install frontend dependencies
echo [3/4] Installing frontend dependencies...
cd frontend
if not exist "node_modules" (
    echo Installing npm packages...
    npm install
    if %errorlevel% neq 0 (
        echo Error: Failed to install frontend dependencies
        pause
        exit /b 1
    )
) else (
    echo Frontend dependencies already installed
)
cd ..

:: Install backend dependencies
echo [4/4] Installing backend dependencies...
cd backend
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Installing Python packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install backend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo ========================================
echo       Starting WritingHouse Services
echo ========================================
echo.

:: Start backend
echo Starting backend server...
start "WritingHouse Backend" cmd /k "cd backend && venv\Scripts\activate.bat && python main.py"

:: Wait for backend to start
echo Waiting for backend to initialize...
timeout /t 3 /nobreak >nul

:: Start frontend
echo Starting frontend server...
start "WritingHouse Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo         Services Started Successfully!
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to exit this window...
pause >nul