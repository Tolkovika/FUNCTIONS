# Importujemy funkcję z modułu
from card_utils import hide


def main():
    # Przykładowy numer karty kredytowej
    card_number = "5290312400019022"

    try:
        # Maskowanie numeru karty
        masked_card = hide(card_number)
        print(f"Zamaskowany numer karty: {masked_card}")
    except ValueError as e:
        # Obsługa błędu, jeśli wystąpi
        print(f"Błąd: {e}")


# Uruchamiamy main(), jeśli skrypt jest uruchomiony bezpośrednio
if __name__ == "__main__":
    main()


