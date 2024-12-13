def f(number: int, even: bool) -> int:
    """
    Computes the sum of the digits of a number, filtering by even or odd digits.

    Args:
        number (int): The number whose digits will be summed.
        even (bool): If True, sum only even digits; if False, sum only odd digits.

    Returns:
        int: The sum of the filtered digits.
    """
    if number < 0:
        raise ValueError("Number must be a non-negative integer.")

    # Convert the number to a string to iterate over its digits
    digits = [int(digit) for digit in str(number)]

    # Filter digits based on the `even` parameter
    if even:
        filtered_digits = [digit for digit in digits if digit % 2 == 0]
    else:
        filtered_digits = [digit for digit in digits if digit % 2 != 0]

    # Return the sum of the filtered digits
    return sum(filtered_digits)

# Test cases
print(f(3124, True))   # Expected output: 6 (3 + 1 + 2 + 4 -> 2 + 4 = 6)
print(f(3124, False))  # Expected output: 4 (3 + 1 + 2 + 4 -> 3 + 1 = 4)
print(f(20576, False)) # Expected output: 12 (2 + 0 + 5 + 7 + 6 -> 5 + 7 = 12)
print(f(20576, True))  # Expected output: 8 (2 + 0 + 5 + 7 + 6 -> 2 + 6 = 8)
print(f(13115, True))  # Expected output: 0 (1 + 3 + 1 + 1 + 5 -> no even digits)
