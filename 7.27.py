def f(product_code: str) -> bool:
    """
    Checks if the product code is correct. The fourth digit is the remainder of
    dividing the sum of the first three digits by 7.

    Args:
        product_code (str): The product code consisting of 4 digits.

    Returns:
        bool: True if the product code is correct, False otherwise.
    """
    # Ensure the product code has 4 digits
    if len(product_code) == 4 and product_code.isdigit():
        # Extract the first three digits and the fourth digit
        first_three_digits = product_code[:3]
        control_digit = int(product_code[3])

        # Calculate the sum of the first three digits
        sum_of_digits = sum(int(digit) for digit in first_three_digits)

        # Calculate the remainder when dividing the sum by 7
        remainder = sum_of_digits % 7

        # Return True if the remainder matches the control digit
        return remainder == control_digit
    return False


print(f("1082"))  # Expected output: True
print(f("2035"))  # Expected output: True
print(f("1114"))  # Expected output: False
print(f("7071"))  # Expected output: False
