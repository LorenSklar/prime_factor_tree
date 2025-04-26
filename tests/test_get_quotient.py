from app.core.get_quotient import get_quotient

def test_valid_division():
    """Test valid division cases"""
    result = get_quotient(10, 2)
    assert result["is_valid"] is True
    assert result["quotient"] == 5
    assert result["error_type"] is None
    assert result["message"] == ""

def test_division_with_remainder():
    """Test division that results in remainder"""
    result = get_quotient(10, 3)
    assert result["is_valid"] is True
    assert result["quotient"] == 3
    assert result["error_type"] is None
    assert result["message"] == ""

def test_invalid_inputs():
    """Test invalid inputs"""
    # Non-number inputs
    result = get_quotient("10", 2)
    assert result["is_valid"] is False
    assert result["quotient"] is None
    assert result["error_type"] == "ValueError"
    
    # Division by zero
    result = get_quotient(10, 0)
    assert result["is_valid"] is False
    assert result["quotient"] is None
    assert result["error_type"] == "ValueError"
    assert "not defined" in result["message"] 