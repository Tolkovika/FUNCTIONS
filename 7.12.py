def f(n: int) -> str:
    """
    Zwraca ciąg gwiazdek oddzielonych ukośnikami.

    Argumenty:
        n (int): Liczba gwiazdek.

    Zwraca:
        str: Ciąg gwiazdek.
    """
    # Jeśli n <= 0, zwracamy pusty ciąg znaków (nie ma gwiazdek do wyświetlenia)
    if n <= 0:
        return ""
    
    # Tworzymy ciąg gwiazdek oddzielonych ukośnikami
    # Przykład: dla n=4: "*/*/*/*"
    return "*/" * (n - 1) + "*"

def main():
    print(f(4))  #wynik: "*/*/*/*"
    print(f(1))  #wynik: "*"
    print(f(0))  #wynik: ""

# Sprawdzamy, czy uruchamiamy plik jako główny skrypt
if __name__ == "__main__":
    main()



