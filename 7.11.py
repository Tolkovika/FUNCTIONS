def f(n1: int, n2: int, n3: int) -> bool:
    """
    Funkcja sprawdza, czy przynajmniej jedna z podanych liczb jest ujemna.

    Argumenty:
        n1 (int): Pierwsza liczba.
        n2 (int): Druga liczba.
        n3 (int): Trzecia liczba.

    Zwraca:
        bool: True, jeśli przynajmniej jedna liczba jest ujemna, False w przeciwnym razie.
    """
    # Sprawdzamy, czy któraś z liczb jest ujemna
    return n1 < 0 or n2 < 0 or n3 < 0

def main():
    # Testujemy funkcję 
    print(f(11, 6, -4))  #  True (bo -4 jest liczbą ujemną)
    print(f(5, 4, 14))   #  False (brak liczb ujemnych)
    print(f(-1, 0, 3))   #  True (bo -1 jest liczbą ujemną)
    print(f(0, 0, 0))    # False (brak liczb ujemnych)
    print(f(-5, -2, -8)) # True (wszystkie liczby są ujemne)

# Jeśli uruchamiamy skrypt bezpośrednio, to wywołujemy main()
if __name__ == "__main__":
    main()