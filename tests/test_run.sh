#!/bin/bash

# Exit on error
set -e

echo "Setting up test environment..."

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "Error: Must run from project root directory"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Add project root to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run tests
echo "Running tests..."
pytest tests/

# Optional: Run with coverage
# echo "Running tests with coverage..."
# pytest --cov=app tests/

echo "Tests completed!" 