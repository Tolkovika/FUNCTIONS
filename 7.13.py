def f(n: int) -> str:
    """
    Zwraca liczby od 1 do n jako jeden połączony ciąg znaków.

    Argumenty:
        n (int): Górna granica zakresu.

    Zwraca:
        str: Połączony ciąg liczb od 1 do n.
    """
    # Jeśli n <= 0, zwracamy pusty ciąg znaków
    if n <= 0:
        return ""
    
    # Tworzymy ciąg liczb od 1 do n połączonych w jeden string
    return "".join(str(i) for i in range(1, n + 1))

def main():
    # Przykładowe testy funkcji
    print(f(11))  # wynik: "1234567891011"
    print(f(4))   # wynik: "1234"
    print(f(0))   # wynik: "" (pusty ciąg)
    print(f(-3))  # wynik: "" (pusty ciąg)
    print(f(1))   # wynik: "1"

# Sprawdzamy, czy uruchamiamy plik jako główny skrypt
if __name__ == "__main__":
    main()

