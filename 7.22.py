def f(name: str) -> str:
    """
    Zwraca akronim utworzony z pierwszych liter każdego słowa w podanym tekście.

    Argumenty:
        name (str): Tekst, z którego mają zostać utworzone litery akronimu.

    Zwraca:
        str: Akronim utworzony z pierwszych liter każdego słowa.
    """
    # dzielimy tekst na słowa, bierzemy pierwszą literę z każdego słowa, a następnie łączymy je w jeden ciąg
    acronym = ''.join(word[0].upper() for word in name.split() if word)

    return acronym

def main():
    print(f("Internet of Things"))  # wynik: "IoT"
    print(f("For Your Information"))  # wynik: "FYI"
    print(f("Python"))  # wynik: "P"

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()