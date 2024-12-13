def f(x: int, y: int) -> int:
    """
    Returns the sum of numbers in the range <x, y> that are divisible by both 2 and 3,
    but not divisible by 4.

    Args:
        x (int): The starting value of the range.
        y (int): The ending value of the range.

    Returns:
        int: The sum of numbers that meet the condition.
    """
    total_sum = 0
    for number in range(x, y + 1):
        if number % 6 == 0 and number % 4 != 0:
            total_sum += number
    return total_sum

print(f(1, 20))   # Expected output: 24
print(f(10, 30))  # Expected output: 48
