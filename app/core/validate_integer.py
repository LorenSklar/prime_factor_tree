def validate_integer(value, name="value", lower=float('-inf'), upper=float('inf')):
    """
    Validate that a value is an integer or convertible to integer within specified bounds.
    
    Args:
        value: The value to validate
        name: A descriptive name for the value
        lower: The lower inclusive bound
        upper: The upper exclusive bound 
        
    Returns:
        Tuple of (bool, str):
        - True, "" if validation succeeds
        - False, error_message if validation fails
    """
    # Check if value is a number
    if not isinstance(value, (int, float)):
        return False, f"{value!r} is not a valid integer for '{name}'."
    
    # Check if float has fractional part
    if isinstance(value, float) and value != int(value):
        return False, f"{value!r} is not a valid integer for '{name}'."
    
    # Convert to integer
    value_as_integer = int(value)
    
    # Check bounds
    if value_as_integer < lower:
        return False, f"{value!r} for '{name}' is below lower bound {lower}."
    if value_as_integer >= upper:
        return False, f"{value!r} for '{name}' is at or above upper bound {upper}."
    
    return True, ""
