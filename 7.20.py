def f(n: int) -> int:
    """
    Returns the n-th prime number.

    Args:
        n (int): The position of the prime number to return.

    Returns:
        int: The n-th prime number.
    """

    def is_prime(num: int) -> bool:
        """Helper function to check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 1

    # Keep finding prime numbers until we reach the n-th one
    while count < n:
        num += 1
        if is_prime(num):
            count += 1

    return num


print(f(1))  # Expected output: 2
print(f(5))  # Expected output: 11
