# importujemy funkcję z modułu
from card_utils import hide


def main():
    card_number = "5290312400019022"

    try:
        # maskowanie numeru karty
        masked_card = hide(card_number)
        print(f"Zamaskowany numer karty: {masked_card}")
    except ValueError as e:
        # obsługa błędu, jeśli wystąpi
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()

