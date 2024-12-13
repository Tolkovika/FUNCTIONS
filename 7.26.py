def f(text: str) -> str:
    """
    Returns the given text with all characters separated by a dash.

    Args:
        text (str): The input text to modify.

    Returns:
        str: The modified text with characters separated by a dash.
    """
    return '-'.join(text) if text else ""

print(f("University"))  # Expected output: "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))          # Expected output: "U-E"
print(f("x"))           # Expected output: "x"
print(f(""))            # Expected output: ""
