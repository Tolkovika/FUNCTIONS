def f(number1: int, number2: int, number3: int) -> int:
    """
    Zwraca różnicę między największą a najmniejszą liczbą.

    Argumenty:
        number1 (int): Pierwsza liczba.
        number2 (int): Druga liczba.
        number3 (int): Trzecia liczba.

    Zwraca:
        int: Różnica między największą a najmniejszą liczbą.
    """
    # zwracamy różnicę między największą a najmniejszą liczbą
    return max(number1, number2, number3) - min(number1, number2, number3)

def main():
    print(f(7, 4, 9))  # wynik: 5 (9 - 4)
    print(f(2, 12, 8))  # wynik: 10 (12 - 2)

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()