@echo off
REM Quick test execution script for Windows

echo ========================================
echo StyleZone Test Automation Framework
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

echo.
echo Running tests...
echo.

REM Run tests with HTML report
pytest --html=reports/report.html --self-contained-html -v

echo.
echo ========================================
echo Tests completed!
echo Check reports/report.html for results
echo ========================================
pause

