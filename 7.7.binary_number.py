def f(binary_number: str) -> bool:
    """
    Sprawdza, czy podany ciąg znaków jest poprawnym liczba binarną.

    Argumenty:
        binary_number (str): Ciąg znaków do sprawdzenia.

    Zwraca:
        bool: True, jeśli ciąg jest poprawną liczbą binarną, False w przeciwnym razie.
    """
    return binary_number != "" and all(char in "01" for char in binary_number)

def main():
    # Testowanie funkcji f()
    print(f("101101"))       # True
    print(f("1311a10100"))   # False
    print(f("001010"))       # True
    print(f(""))             # False

# Dodanie warunku uruchamiania programu
if __name__ == "__main__":
    main()

