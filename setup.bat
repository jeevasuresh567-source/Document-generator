@echo off
cd /d "%~dp0"
if not exist "venv\Scripts\python.exe" py -3 -m venv venv
if errorlevel 1 (echo Failed to create venv & pause & exit /b 1)
call "venv\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if not exist ".env" copy ".env.example" ".env" >nul
echo Setup complete.
pause
