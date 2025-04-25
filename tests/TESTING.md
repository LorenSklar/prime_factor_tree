# Testing Guide

## Quick Start

The easiest way to run tests is using the provided script:

```bash
# First, navigate to the project root directory (where README.md is located)
cd /path/to/prime_factors

# Verify you're in the right directory
ls  # Should show README.md, app/, tests/, etc.

# Run tests from the project root
bash tests/test_run.sh
```

This script will:
1. Check if you're in the correct directory
2. Create and activate a virtual environment
3. Install/upgrade dependencies
4. Set the project root directory as prime_factors so that Python imports modules properly
5. Run all tests

## Manual Setup

If you need to run tests manually:

### 1. Navigate to Project Directory
```bash
# Navigate to project root
cd /path/to/prime_factors

# Verify you're in the right directory
ls  # Should show README.md, app/, tests/, etc.
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install requirements
pip install -r requirements.txt
```

### 4. Set Python Path

```bash
# Add project root to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

This sets the current directory (prime_factors) as the root directory for Python imports. This means when we write `from app.core.validate_integer import validate_integer`, Python knows to look for the `app` folder starting from the prime_factors directory.

## Running Tests Manually

If you need more control, you can run tests directly from the project root:

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/

# Run with print statements visible
pytest -s tests/

# Run with coverage
pytest --cov=app tests/
```

### Specific Test Files
```bash
# Run specific test file
pytest tests/test_validate_integer.py

# Run specific test function
pytest tests/test_validate_integer.py::test_valid_integer
```

## Test Structure

- `tests/`: Contains all test files
- Each test file corresponds to a module in `app/`
- Test functions are prefixed with `test_`
- Test files are prefixed with `test_`

## Writing Tests

1. Import the module to test:
```python
from app.core.validate_integer import validate_integer
```

2. Write test functions:
```python
def test_valid_integer():
    assert validate_integer(42) == (True, "")
```

3. Use descriptive test names
4. Include docstrings explaining test purpose
5. Test both success and failure cases

## Best Practices

1. Keep tests independent
2. Test one thing per test function
3. Use meaningful assertions
4. Include edge cases
5. Test error messages
6. Keep tests simple and readable 