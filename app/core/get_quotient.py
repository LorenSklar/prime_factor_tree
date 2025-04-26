from app.core.config import LOWER_LIMIT, UPPER_LIMIT
from app.core.validate_integer import validate_integer

def get_quotient(dividend, divisor):
    """
    Calculate the quotient of the division between dividend and divisor,
    with input validation and handling for division by zero.

    Args:
        dividend (int | float): The number to be divided.
        divisor (int | float): The number to divide by.

    Returns:
        dict:
            - is_valid (bool): True if valid inputs and no error occurred.
            - quotient (int): The result of the division.
            - error_type (str | None): Type of error, if any.
            - message (str): Explanation or error message.
    """
    # Validate dividend
    dividend_validation = validate_integer(dividend, name="dividend", lower=LOWER_LIMIT, upper=UPPER_LIMIT)
    if not dividend_validation["is_valid"]:
        return {
            "is_valid": False,
            "quotient": None,
            "error_type": dividend_validation["error_type"],
            "message": dividend_validation["message"]
        }

    # Validate divisor
    divisor_validation = validate_integer(divisor, name="divisor", lower=LOWER_LIMIT, upper=UPPER_LIMIT)
    if not divisor_validation["is_valid"]:
        return {
            "is_valid": False,
            "quotient": None,
            "error_type": divisor_validation["error_type"],
            "message": divisor_validation["message"]
        }

    # Handle divide by zero
    if int(divisor) == 0:
        return {
            "is_valid": False,
            "quotient": None,
            "error_type": "ValueError",
            "message": f"{dividend} ÷ {divisor} is not defined"
        }

    # Calculate quotient
    quotient = int(dividend) // int(divisor)  # Integer division
    return {
        "is_valid": True,
        "quotient": quotient,
        "error_type": None,
        "message": ""
    }