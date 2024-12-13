# main.py

# Import the function from the module
from card_utils import hide


def main():
    # Example credit card number
    card_number = "5290312400019022"

    try:
        masked_card = hide(card_number)
        print(f"Masked Card Number: {masked_card}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
