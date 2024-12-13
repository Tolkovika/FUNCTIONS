def f(n1: int, n2: int, n3: int) -> bool:
    """
    Checks if at least one of the given numbers is negative.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        n3 (int): The third number.

    Returns:
        bool: True if at least one number is negative, False otherwise.
    """
    return n1 < 0 or n2 < 0 or n3 < 0

# Test cases
print(f(11, 6, -4))  # Expected output: True (because -4 is negative)
print(f(5, 4, 14))   # Expected output: False (no negative numbers)
print(f(-1, 0, 3))   # Expected output: True (because -1 is negative)
print(f(0, 0, 0))    # Expected output: False (no negative numbers)
print(f(-5, -2, -8)) # Expected output: True (all are negative)
