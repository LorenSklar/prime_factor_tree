import pytest
from app.core.validate_integer import validate_integer

def test_valid_integer():
    """Test valid integer inputs"""
    assert validate_integer(42) == (True, "")
    assert validate_integer(0) == (True, "")
    assert validate_integer(-1) == (True, "")

def test_valid_float():
    """Test valid float inputs that are convertible to integers"""
    assert validate_integer(42.0) == (True, "")
    assert validate_integer(0.0) == (True, "")
    assert validate_integer(-1.0) == (True, "")

def test_invalid_inputs():
    """Test invalid inputs"""
    # Non-number inputs
    assert validate_integer("dog")[0] is False
    assert validate_integer("42")[0] is False
    assert validate_integer(None)[0] is False
    assert validate_integer([])[0] is False
    
    # Floats with fractional parts
    assert validate_integer(42.5)[0] is False
    assert validate_integer(0.1)[0] is False
    assert validate_integer(-1.9)[0] is False

def test_bounds():
    """Test boundary conditions"""
    # Within bounds
    assert validate_integer(5, lower=0, upper=10) == (True, "")
    assert validate_integer(0, lower=0, upper=10) == (True, "")
    assert validate_integer(9, lower=0, upper=10) == (True, "")
    
    # Below lower bound
    result, msg = validate_integer(-1, lower=0, upper=10)
    assert result is False
    assert "below lower bound" in msg
    
    # At or above upper bound
    result, msg = validate_integer(10, lower=0, upper=10)
    assert result is False
    assert "at or above upper bound" in msg

def test_error_messages():
    """Test error message content"""
    # Non-number
    _, msg = validate_integer("dog", name="test")
    assert "test" in msg
    assert "not a valid integer" in msg
    
    # Fractional part
    _, msg = validate_integer(42.5, name="test")
    assert "test" in msg
    assert "not a valid integer" in msg
    
    # Out of bounds
    _, msg = validate_integer(11, name="test", lower=0, upper=10)
    assert "test" in msg
    assert "at or above upper bound" in msg 