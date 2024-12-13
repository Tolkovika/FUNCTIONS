def f(n: int) -> int:
    """
    Zwraca n-tą liczbę w ciągu Fibonacciego.

    Argumenty:
        n (int): Pozycja liczby Fibonacciego do zwrócenia.

    Zwraca:
        int: n-ta liczba Fibonacciego.
    """
    if n == 1:
        return 0  # Pierwsza liczba Fibonacciego
    elif n == 2:
        return 1  # Druga liczba Fibonacciego

    a, b = 0, 1  # Początkowe wartości dla pierwszych dwóch liczb
    for _ in range(3, n + 1):
        a, b = b, a + b  # Aktualizujemy a i b, aby uzyskać kolejną parę liczb Fibonacciego

    return b

def main():
    print(f(5))  # wynik: 3
    print(f(9))  # wynik: 21

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()
