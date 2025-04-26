from app.core.config import LOWER_LIMIT, UPPER_LIMIT
from app.core.validate_integer import validate_integer

def get_remainder(dividend, divisor):
    """
    Calculate the remainder of the division between dividend and divisor,
    with input validation and handling for division by zero.

    Args:
        dividend (int | float): The number to be divided.
        divisor (int | float): The number to divide by.

    Returns:
        dict:
            - is_valid (bool): True if valid inputs and no error occurred.
            - remainder (int): The remainder of the division.
            - error_type (str | None): Type of error, if any.
            - message (str): Explanation or error message.
    """
    # Validate dividend
    dividend_validation = validate_integer(dividend, name="dividend", lower=LOWER_LIMIT, upper=UPPER_LIMIT)
    if not dividend_validation["is_valid"]:
        return {
            "is_valid": False,
            "remainder": None,
            "error_type": dividend_validation["error_type"],
            "message": dividend_validation["message"]
        }

    # Validate divisor
    divisor_validation = validate_integer(divisor, name="divisor", lower=LOWER_LIMIT, upper=UPPER_LIMIT)
    if not divisor_validation["is_valid"]:
        return {
            "is_valid": False,
            "remainder": None,
            "error_type": divisor_validation["error_type"],
            "message": divisor_validation["message"]
        }

    # Handle divide by zero
    if int(divisor) == 0:
        return {
            "is_valid": False,
            "remainder": None,
            "error_type": "ValueError",
            "message": f"Division by zero is not defined"
        }

    # Calculate remainder
    remainder = int(dividend) % int(divisor)  # Modulus operation for remainder
    return {
        "is_valid": True,
        "remainder": remainder,
        "error_type": None,
        "message": ""
    }