def f(palindrome: str) -> bool:
    """
    Zwraca True, jeśli podany ciąg jest palindromem, w przeciwnym razie False.

    Argumenty:
        palindrome (str): Ciąg znaków do sprawdzenia, czy jest palindromem.

    Zwraca:
        bool: True, jeśli ciąg jest palindromem, False w przeciwnym razie.
    """
    # usuwamy wszystkie znaki niealfanumeryczne i konwertujemy na małe litery
    cleaned_str = ''.join(char.lower() for char in palindrome if char.isalnum())

    #czy ciąg jest równy swojemu odwróconemu odpowiednikowi
    return cleaned_str == cleaned_str[::-1]

def main():
    print(f("radar"))      # wynik: True
    print(f("12-11-21"))   # wynik: True
    print(f("book"))       # wynik: False

if __name__ == "__main__":
    main()