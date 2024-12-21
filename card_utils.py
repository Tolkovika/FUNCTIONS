def hide(card_number: str) -> str:  #maskuje
    if len(card_number) != 16 or not card_number.isdigit(): #nie ma 16 i nie zawiera litery
        raise ValueError("Card number must be a string of exactly 16 digits.")

    return card_number[:2] + '*' * 10 + card_number[-4:]  #pierwsze 2 10* i 4 ostatnie
