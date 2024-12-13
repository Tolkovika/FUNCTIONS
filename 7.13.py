def f(n: int) -> str:
    """
    Returns numbers from 1 to n as a concatenated string.

    Args:
        n (int): The upper limit of the range.

    Returns:
        str: A concatenated string of numbers from 1 to n.
    """
    if n <= 0:
        return ""  # Return an empty string if n is less than or equal to 0
    return "".join(str(i) for i in range(1, n + 1))

# Test cases
print(f(11))  # Expected output: "1234567891011"
print(f(4))   # Expected output: "1234"
print(f(0))   # Expected output: "" (empty string)
print(f(-3))  # Expected output: "" (empty string)
print(f(1))   # Expected output: "1"
