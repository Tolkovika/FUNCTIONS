def f(n: int) -> int:
    """
    Returns the n-th value of the Fibonacci sequence.

    Args:
        n (int): The position of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n == 1:
        return 0  # First Fibonacci number
    elif n == 2:
        return 1  # Second Fibonacci number

    a, b = 0, 1  # Starting values for the first two numbers
    for _ in range(3, n + 1):
        a, b = b, a + b  # Update a and b to the next pair of Fibonacci numbers

    return b

print(f(5))  # Expected output: 3
print(f(9))  # Expected output: 21
