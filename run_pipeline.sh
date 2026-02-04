#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

echo "--- [$(date)] Starting Industrial ETL Automation ---"

if [ ! -d "data/CMaps" ]; then
    echo "ERROR: Data directory not found. Please download NASA dataset."
    exit 1
fi

echo "Checking dependencies..."
pip install -q -r requirements.txt

echo "Running Extract, Transform, Validate, and Load..."
python src/main.py

echo "--- [$(date)] Pipeline Execution Successful ---"