if __name__ == "__main__":
    from card_number import hide

    card_number = "5290312400019022"
    masked_card = hide(card_number)

    if masked_card:
        print(masked_card)