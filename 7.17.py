def f(palindrome: str) -> bool:
    """
    Returns True if the given string is a palindrome, False otherwise.

    Args:
        palindrome (str): The string to check for palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in palindrome if char.isalnum())

    # Check if the string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]


print(f("radar"))      # Expected output: True
print(f("12-11-21"))   # Expected output: True
print(f("book"))       # Expected output: False
