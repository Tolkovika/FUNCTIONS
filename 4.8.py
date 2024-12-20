def f(n: int) -> str:
    """
    Zwraca ciąg gwiazdek oddzielonych ukośnikami.

    Argumenty:
        n (int): Liczba gwiazdek.

    Zwraca:
        str: Ciąg gwiazdek.
    """
    if n <= 0:
        return ""  # Pusty ciąg dla n <= 0
    return "/*" * (n - 1) + "*"  # Dodajemy gwiazdki

def main():
    # Testy funkcji f()
    print(f(4))  # "*/*/*/*"
    print(f(1))  # "*"
    print(f(0))  # ""
    print(f(-3)) # ""
    print(f(6))  # "*/*/*/*/*/*"

# Uruchamiamy funkcję main() tylko jeśli skrypt jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()
