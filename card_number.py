def hide(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        print("Error: Card number must be exactly 16 digits.")
        return None

    first_two = card_number[:2]
    last_four = card_number[-4:]
    masked_middle = '*' * 10

    return first_two + masked_middle + last_four