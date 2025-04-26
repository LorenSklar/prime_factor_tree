def validate_integer(value, name="value", lower=float('-inf'), upper=float('inf')):
    """
    Validate that a value is an integer or convertible to integer within specified bounds.
    
    Args:
        value: The value to validate.
        name: A descriptive name for the value (e.g., 'dividend', 'divisor').
        lower: The lower inclusive bound.
        upper: The upper exclusive bound.
        
    Returns:
        dict:
            - is_valid (bool): True if the value is valid.
            - error_type (str | None): The error type if validation fails.
            - message (str): An error message if validation fails.
    """
    # Check if value is a number
    if not isinstance(value, (int, float)):
        return {
            "is_valid": False,
            "error_type": "ValueError",
            "message": f"{value!r} is not a valid integer for '{name}'."
        }
    
    # Check if float has fractional part
    if isinstance(value, float) and value != int(value):
        return {
            "is_valid": False,
            "error_type": "ValueError",
            "message": f"{value!r} is not a valid integer for '{name}'."
        }
    
    # Convert to integer
    value_as_integer = int(value)
    
    # Check bounds
    if value_as_integer < lower:
        return {
            "is_valid": False,
            "error_type": "ValueError",
            "message": f"{value!r} for '{name}' is below lower bound {lower}."
        }
    if value_as_integer >= upper:
        return {
            "is_valid": False,
            "error_type": "ValueError",
            "message": f"{value!r} for '{name}' is at or above upper bound {upper}."
        }
    
    # Return success if all checks pass
    return {
        "is_valid": True,
        "error_type": None,
        "message": ""
    }
