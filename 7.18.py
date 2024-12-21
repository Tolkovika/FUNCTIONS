def f(sentence: str) -> str:
    """
    Zwraca zdanie bez spacji.

    Argumenty:
        sentence (str): Zdanie, z którego mają zostać usunięte spacje.

    Zwraca:
        str: Zdanie bez spacji.
    """
    # usuwamy wszystkie spacje w zdaniu
    return sentence.replace(" ", "")

def main():
    print(f("integrated development environment"))  

    print(f("A programming language is a system of notation for writing computer programs"))  

if __name__ == "__main__":
    main()