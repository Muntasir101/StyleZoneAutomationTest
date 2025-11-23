#!/bin/bash
# Quick test execution script for Linux/Mac

echo "========================================"
echo "StyleZone Test Automation Framework"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo ""
echo "Running tests..."
echo ""

# Run tests with HTML report
pytest --html=reports/report.html --self-contained-html -v

echo ""
echo "========================================"
echo "Tests completed!"
echo "Check reports/report.html for results"
echo "========================================"

