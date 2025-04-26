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

# Default test command
TEST_CMD="pytest tests/"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            TEST_CMD="$TEST_CMD -v"
            shift
            ;;
        -s|--show-output)
            TEST_CMD="$TEST_CMD -s"
            shift
            ;;
        -c|--coverage)
            TEST_CMD="$TEST_CMD --cov=app"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Run tests
echo "Running tests..."
$TEST_CMD

echo "Tests completed!" 