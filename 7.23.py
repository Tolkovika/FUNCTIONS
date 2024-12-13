def f(password: str) -> bool:
    """
    Returns True if the password is valid. A valid password should have at least six characters
    and each character should appear only once. Otherwise, returns False.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Check if the password length is at least 6 and if all characters are unique
    if len(password) >= 6 and len(set(password)) == len(password):
        return True
    return False

print(f("ax15"))       # Expected output: False (less than 6 characters)
print(f("book123"))    # Expected output: False (duplicate 'o' character)
print(f("A2water3"))   # Expected output: True (valid password)
print(f("qwerty"))     # Expected output: True (valid password)
print(f(""))           # Expected output: False (empty password)
