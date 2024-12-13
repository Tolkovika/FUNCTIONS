def f(number1: int, number2: int, number3: int) -> int:
    """
    Returns the difference between the largest and smallest numbers.

    Args:
        number1 (int): First number.
        number2 (int): Second number.
        number3 (int): Third number.

    Returns:
        int: The difference between the largest and smallest numbers.
    """
    return max(number1, number2, number3) - min(number1, number2, number3)

print(f(7, 4, 9))  # Expected output: 5 (9 - 4)
print(f(2, 12, 8))  # Expected output: 10 (12 - 2)
