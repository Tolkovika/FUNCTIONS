def f(sentence: str) -> str:
    """
    Zwraca zdanie bez spacji.

    Argumenty:
        sentence (str): Zdanie, z którego mają zostać usunięte spacje.

    Zwraca:
        str: Zdanie bez spacji.
    """
    # Usuwamy wszystkie spacje w zdaniu
    return sentence.replace(" ", "")

def main():
    # Testowanie funkcji
    print(f("integrated development environment"))  
    #wynik: "integrateddevelopmentenvironment"

    print(f("A programming language is a system of notation for writing computer programs"))  
    #wynik: "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()