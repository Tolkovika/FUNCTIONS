def f(number: int, even: bool) -> int:
    """
    Funkcja oblicza sumę cyfr liczby, wybierając tylko cyfry parzyste lub nieparzyste.

    Argumenty:
        number (int): Liczba, z której sumujemy cyfry.
        even (bool): Jeśli True, sumujemy tylko cyfry parzyste; jeśli False, sumujemy tylko cyfry nieparzyste.

    Zwraca:
        int: Suma przefiltrowanych cyfr.
    """
    # Sprawdzamy, czy liczba nie jest ujemna
    if number < 0:
        raise ValueError("Liczba musi być liczbą nieujemną.")

    # Przekształcamy liczbę na listę cyfr, żeby łatwiej było je przetwarzać
    digits = [int(digit) for digit in str(number)]

    # Filtrujemy cyfry - parzyste lub nieparzyste
    if even:
        filtered_digits = [digit for digit in digits if digit % 2 == 0]  # Cyfry parzyste
    else:
        filtered_digits = [digit for digit in digits if digit % 2 != 0]  # Cyfry nieparzyste

    # Zwracamy sumę wybranych cyfr
    return sum(filtered_digits)

def main():
    # Testujemy funkcję f() z różnymi danymi
    print(f(3124, True))   # Powinno dać wynik: 6 (bo 2 + 4 = 6)
    print(f(3124, False))  # Powinno dać wynik: 4 (bo 3 + 1 = 4)
    print(f(20576, False)) # Powinno dać wynik: 12 (bo 5 + 7 = 12)
    print(f(20576, True))  # Powinno dać wynik: 8 (bo 2 + 6 = 8)
    print(f(13115, True))  # Powinno dać wynik: 0 (bo nie ma cyfr parzystych)

# Jeśli uruchamiamy skrypt bezpośrednio, to wywołujemy main()
if __name__ == "__main__":
    main()
