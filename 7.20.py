def f(n: int) -> int:
    """
    Zwraca n-tą liczbę pierwszą.

    Argumenty:
        n (int): Pozycja liczby pierwszej, którą mamy zwrócić.

    Zwraca:
        int: n-ta liczba pierwsza.
    """

    def is_prime(num: int) -> bool:
        """Funkcja pomocnicza do sprawdzania, czy liczba jest liczbą pierwszą."""
        if num <= 1:
            return False  # Liczby mniejsze lub równe 1 nie są pierwsze
        for i in range(2, int(num ** 0.5) + 1):  # Sprawdzamy dzielniki do pierwiastka z num
            if num % i == 0:  # Jeśli num dzieli się przez i, to nie jest liczbą pierwszą
                return False
        return True  # Liczba jest pierwsza

    count = 0  # liczymy liczbę pierwszych
    num = 1  # początkowa liczba

    # Dopóki nie znajdziemy n-tej liczby pierwszej
    while count < n:
        num += 1  # zwiększamy liczbę
        if is_prime(num):  # sprawdzamy czy jest liczbą pierwszą
            count += 1  # jeśli jest pierwsza zwiększamy licznik

    return num  # Zwracamy n-tą liczbę pierwszą

def main():
    print(f(1))  #wynik: 2 (pierwsza liczba pierwsza)
    print(f(5))  #wynik: 11 (piąta liczba pierwsza)

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()
