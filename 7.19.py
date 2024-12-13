from collections import Counter


def f(number: int) -> int:
    """
    Returns the sum of repeated digits in the given number.

    Args:
        number (int): The number to check for repeated digits.

    Returns:
        int: The sum of repeated digits.
    """
    # Convert the number to a string to easily iterate through its digits
    str_number = str(number)

    # Count the frequency of each digit
    digit_count = Counter(str_number)

    # Calculate the sum of repeated digits
    sum_repeated_digits = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)

    return sum_repeated_digits

print(f(1027))        # Expected output: 0 (no repeated digits)
print(f(230335))      # Expected output: 9 (3 + 3 + 3)
print(f(513553007))   # Expected output: 21 (5 + 5 + 3 + 3 + 0 + 0)
