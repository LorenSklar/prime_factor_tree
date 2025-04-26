from app.core.get_remainder import get_remainder

def test_valid_division():
    """Test valid division cases"""
    result = get_remainder(10, 2)
    assert result["is_valid"] is True
    assert result["remainder"] == 0
    assert result["error_type"] is None
    assert result["message"] == ""

def test_division_with_remainder():
    """Test division that results in remainder"""
    result = get_remainder(10, 3)
    assert result["is_valid"] is True
    assert result["remainder"] == 1
    assert result["error_type"] is None
    assert result["message"] == ""

def test_invalid_inputs():
    """Test invalid inputs"""
    # Non-number inputs
    result = get_remainder("10", 2)
    assert result["is_valid"] is False
    assert result["remainder"] is None
    assert result["error_type"] == "ValueError"
    
    # Division by zero
    result = get_remainder(10, 0)
    assert result["is_valid"] is False
    assert result["remainder"] is None
    assert result["error_type"] == "ValueError"
    assert "not defined" in result["message"] 