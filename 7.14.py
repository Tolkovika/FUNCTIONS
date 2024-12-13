def f(number1: float, number2: float, operator: str) -> float:
    """
    Performs an arithmetic operation on two numbers based on the given operator.

    Args:
        number1 (float): The first number.
        number2 (float): The second number.
        operator (str): The arithmetic operator (+, -, *, %, **).

    Returns:
        float: The result of the arithmetic operation.
    """
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        raise ValueError("Unsupported operator. Use one of +, -, *, %, **.")


# Test cases
print(f(2, 3, "+"))   # Expected output: 5
print(f(2, 3, "%"))   # Expected output: 2
print(f(2, 3, "**"))  # Expected output: 8
print(f(2, 3, "*"))   # Expected output: 6
print(f(2, 3, "-"))   # Expected output: -1
