from app.core.is_divisible import is_divisible

def test_valid_division():
    """Test valid division cases"""
    result = is_divisible(10, 2)
    assert result["is_valid"] is True
    assert result["is_divisible"] is True
    assert result["error_type"] is None
    assert result["message"] == ""

def test_not_divisible():
    """Test cases where numbers are not divisible"""
    result = is_divisible(10, 3)
    assert result["is_valid"] is True
    assert result["is_divisible"] is False
    assert result["error_type"] is None
    assert result["message"] == ""

def test_invalid_inputs():
    """Test invalid inputs"""
    # Non-number inputs
    result = is_divisible("10", 2)
    assert result["is_valid"] is False
    assert result["is_divisible"] is None
    assert result["error_type"] == "ValueError"
    
    # Division by zero
    result = is_divisible(10, 0)
    assert result["is_valid"] is False
    assert result["is_divisible"] is None
    assert result["error_type"] == "ValueError"
    assert "not defined" in result["message"] 