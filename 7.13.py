def f(n: int) -> str:
    """
    Zwraca liczby od 1 do n jako jeden połączony ciąg znaków.

    Argumenty:
        n (int): Górna granica zakresu.

    Zwraca:
        str: Połączony ciąg liczb od 1 do n.
    """
    # jeśli n <= 0 zwracamy pusty ciąg znaków
    if n <= 0:
        return ""
    
    # tworzymy ciąg liczb od 1 do n połączonych w jeden string
    return "".join(str(i) for i in range(1, n + 1))

def main():
    print(f(11))  
    print(f(4))   
    print(f(0))   
    print(f(-3))  
    print(f(1))   

# uruchamiamy plik jako główny skrypt
if __name__ == "__main__":
    main()