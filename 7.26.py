def f(text: str) -> str:
    """
    Zwraca ciąg znaków, w którym każdy znak z tekstu jest oddzielony myślnikiem.

    Argumenty:
        text (str): Tekst, w którym znaki mają być rozdzielone myślnikami.

    Zwraca:
        str: Ciąg znaków oddzielonych myślnikami.
    """
    # sprawdzamy, czy tekst nie jest pusty
    return '-'.join(text) if text else ""  # lączymy znaki myślnikami, jeśli tekst nie jest pusty, w przeciwnym razie zwracamy pusty ciąg.

def main():
    print(f("University"))  
    print(f("UE"))          
    print(f("x"))           
    print(f(""))           

if __name__ == "__main__":
    main()