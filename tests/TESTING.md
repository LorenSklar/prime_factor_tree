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

## Test Options

The test script supports several options:

```bash
# Run all tests
./tests/test_run.sh

# Run with verbose output
./tests/test_run.sh -v

# Run with print statements visible
./tests/test_run.sh -s

# Run with coverage
./tests/test_run.sh -c

# Combine options
./tests/test_run.sh -v -c
```

## Test Structure

- `tests/`: Contains all test files
- Each test file corresponds to a module in `app/`
- Test functions are prefixed with `test_`
- Test files are prefixed with `test_`

### Current Test Files
- `test_validate_integer.py`: Tests for integer validation
- `test_is_divisible.py`: Tests for divisibility checking
- `test_get_quotient.py`: Tests for quotient calculation
- `test_get_remainder.py`: Tests for remainder calculation

## Writing Tests

1. Import the module to test:
```python
from app.core.validate_integer import validate_integer
```

2. Write test functions:
```python
def test_valid_integer():
    result = validate_integer(42)
    assert result["is_valid"] is True
    assert result["error_type"] is None
    assert result["message"] == ""
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