# Learning Track

## Python Concepts

### Environment and Imports
- `PYTHONPATH`: Setting project root for imports
  ```bash
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  ```
- `import os`: For environment variables and path operations
- `from typing import Tuple, Optional`: For type hints

### Testing
- `pytest`: Test framework
- `assert`: Basic test assertions
- `pytest -v`: Verbose output
- `pytest -s`: Show print statements

### Project Structure
- `__init__.py`: Makes directories into packages
- Virtual environment setup
- Requirements management

## Implementation Patterns

### Function Design
- Pure functions
- Type hints
- Error handling
- Return tuples for multiple values

### Testing Patterns
- One test per function
- Test both success and failure cases
- Clear test names
- Good docstrings

## Common Gotchas
- Python path issues
- Virtual environment activation
- Import errors
- Case sensitivity in filenames

## Quick Reference

### Git Commands
```bash
git init
git add .
git commit -m "message"
git remote add origin <url>
git push -u origin main
```

### Python Path
```bash
# Check current path
echo $PYTHONPATH

# Add to path
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate  # Unix
.\venv\Scripts\activate   # Windows

# Deactivate
deactivate
```

### Testing
```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_file.py

# Run with coverage
pytest --cov=app tests/
``` 