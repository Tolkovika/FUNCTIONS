def f(amount_to_pay: int) -> int:
    """
    Oblicza minimalną liczbę monet potrzebnych do zapłacenia określonej kwoty.

    Argumenty:
        amount_to_pay (int): Całkowita kwota do zapłaty (w PLN).

    Zwraca:
        int: Minimalna liczba monet potrzebnych do zapłaty.
    """
    # sprawdzenie, czy kwota jest nieujemna
    if amount_to_pay < 0:
        raise ValueError("Kwota do zapłaty musi być liczbą całkowitą nieujemną.")

    # Dostępne nominały monet w porządku malejącym
    coins = [5, 2, 1]
    num_coins = 0

    # Obliczanie minimalnej liczby monet
    for coin in coins:
        num_coins += amount_to_pay // coin  
        amount_to_pay %= coin  # aktualizujemy pozostałą kwotę do zapłaty

    return num_coins

def main():
    # Testowanie funkcji f()
    print(f(23))  #  6 (4×5 PLN, 1×2 PLN, 1×1 PLN)
    print(f(8))   #  3 (1×5 PLN, 1×2 PLN, 1×1 PLN)
    print(f(2))   #  1 (1×2 PLN)
    print(f(0))   #  0 (brak monet)

# Dodanie warunku uruchamiania programu
if __name__ == "__main__":
    main()
