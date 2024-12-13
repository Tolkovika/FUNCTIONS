def f(binary_number: str) -> bool:
    """
    Checks if the given string is a valid binary number.

    Args:
        binary_number (str): The string to check.

    Returns:
        bool: True if the string is a valid binary number, False otherwise.
    """
    return binary_number != "" and all(char in "01" for char in binary_number)

print(f("101101"))       # True
print(f("1311a10100"))   # False
print(f("001010"))       # True
print(f(""))             # False
