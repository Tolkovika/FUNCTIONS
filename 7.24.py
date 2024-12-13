def f(expression: str) -> int:
    """
    Evaluates an arithmetic expression consisting of single-digit numbers and '+'/'-' operators.

    Args:
        expression (str): The arithmetic expression to evaluate.

    Returns:
        int: The result of the evaluated expression.
    """
    # Ensure the expression contains only digits and + or - operators
    if all(c.isdigit() or c in '+-' for c in expression):
        return eval(expression)  # Evaluate and return the result of the expression
    else:
        raise ValueError("Invalid expression")

print(f("2+3"))        # Expected output: 5
print(f("3+8+1"))      # Expected output: 12
print(f("2+3-4+5-0"))  # Expected output: 6
