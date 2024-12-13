def f(name: str) -> str:
    """
    Returns the acronym formed by the first letters of each word in the input text.

    Args:
        name (str): The input text to form the acronym from.

    Returns:
        str: The acronym formed by the first letters of each word.
    """
    # Split the name into words and get the first letter of each word, then join them
    acronym = ''.join(word[0].upper() for word in name.split() if word)

    return acronym

print(f("Internet of Things"))  # Expected output: "IoT"
print(f("For Your Information"))  # Expected output: "FYI"
print(f("Python"))  # Expected output: "P"
