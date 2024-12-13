def f(palindrome: str) -> bool:
    """
    Zwraca True, jeśli podany ciąg jest palindromem, w przeciwnym razie False.

    Argumenty:
        palindrome (str): Ciąg znaków do sprawdzenia, czy jest palindromem.

    Zwraca:
        bool: True, jeśli ciąg jest palindromem, False w przeciwnym razie.
    """
    # Usuwamy wszystkie znaki niealfanumeryczne i konwertujemy na małe litery
    cleaned_str = ''.join(char.lower() for char in palindrome if char.isalnum())

    # Sprawdzamy, czy ciąg jest równy swojemu odwróconemu odpowiednikowi
    return cleaned_str == cleaned_str[::-1]

def main():
    print(f("radar"))      # wynik: True
    print(f("12-11-21"))   # wynik: True
    print(f("book"))       # wynik: False

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()
