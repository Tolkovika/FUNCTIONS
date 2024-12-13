def f(n: int) -> str:
    """
    Returns a string of n asterisks separated by a slash ('/').

    Args:
        n (int): The number of asterisks to include.

    Returns:
        str: A string of n asterisks separated by a slash.
    """
    if n <= 0:
        return ""  # Return an empty string if n is less than or equal to 0
    return "/*" * (n - 1) + "*" if n > 0 else ""

# Test cases
print(f(4))  # Expected output: "*/*/*/*"
print(f(1))  # Expected output: "*"
print(f(0))  # Expected output: ""
print(f(-3)) # Expected output: ""
print(f(6))  # Expected output: "*/*/*/*/*/*"
