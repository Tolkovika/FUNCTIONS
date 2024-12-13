# card_utils.py

def hide(card_number: str) -> str:
    """
    Masks the credit card number, showing only the first two and last four digits.
    The rest of the digits are replaced with asterisks.

    Args:
        card_number (str): A string representing the credit card number (16 digits).

    Returns:
        str: The masked credit card number.
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Card number must be a string of exactly 16 digits.")

    return card_number[:2] + '*' * 10 + card_number[-4:]
