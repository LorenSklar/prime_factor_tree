import pytest
from app.core.validate_integer import validate_integer

def test_valid_integer():
    """Test valid integer inputs"""
    result = validate_integer(42)
    assert result["is_valid"] is True
    assert result["error_type"] is None
    assert result["message"] == ""

def test_valid_float():
    """Test valid float inputs that are convertible to integers"""
    result = validate_integer(42.0)
    assert result["is_valid"] is True
    assert result["error_type"] is None
    assert result["message"] == ""

def test_invalid_inputs():
    """Test invalid inputs"""
    # Non-number inputs
    result = validate_integer("42", name="test")
    assert result["is_valid"] is False
    assert result["error_type"] == "ValueError"
    assert "test" in result["message"]
    
    # Floats with fractional parts
    result = validate_integer(42.5, name="test")
    assert result["is_valid"] is False
    assert result["error_type"] == "ValueError"
    assert "test" in result["message"]

def test_bounds():
    """Test boundary conditions"""
    # Within bounds
    result = validate_integer(5, lower=0, upper=10)
    assert result["is_valid"] is True
    assert result["error_type"] is None
    assert result["message"] == ""
    
    # At lower bound
    result = validate_integer(0, lower=0, upper=10)
    assert result["is_valid"] is True
    assert result["error_type"] is None
    assert result["message"] == ""
    
    # Below lower bound
    result = validate_integer(-1, lower=0, upper=10)
    assert result["is_valid"] is False
    assert result["error_type"] == "ValueError"
    assert "below lower bound" in result["message"]
    
    # At upper bound
    result = validate_integer(10, lower=0, upper=10)
    assert result["is_valid"] is False
    assert result["error_type"] == "ValueError"
    assert "at or above upper bound" in result["message"]
    
    # Above upper bound
    result = validate_integer(11, lower=0, upper=10)
    assert result["is_valid"] is False
    assert result["error_type"] == "ValueError"
    assert "at or above upper bound" in result["message"]

def test_error_messages():
    """Test error message content"""
    # Non-number
    result = validate_integer("dog", name="test")
    assert "test" in result["message"]
    assert "not a valid integer" in result["message"]
    
    # Fractional part
    result = validate_integer(42.5, name="test")
    assert "test" in result["message"]
    assert "not a valid integer" in result["message"]
    
    # Out of bounds
    result = validate_integer(11, name="test", lower=0, upper=10)
    assert "test" in result["message"]
    assert "at or above upper bound" in result["message"] 