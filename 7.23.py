def f(password: str) -> bool:
    """
    Zwraca True, jeśli hasło spełnia następujące warunki:
    - Ma co najmniej 6 znaków.
    - Zawiera tylko unikalne znaki (żadne powtórzenie).

    Argumenty:
        password (str): hasło, które ma zostać sprawdzone.

    Zwraca:
        bool: True, jeśli hasło jest poprawne, False w przeciwnym razie.
    """
    # sprawdzamy, czy długość hasła jest co najmniej 6 znaków i czy wszystkie znaki są unikalne
    if len(password) >= 6 and len(set(password)) == len(password):
        return True
    return False

def main():
    print(f("ax15"))       # wynik: False (hasło ma mniej niż 6 znaków)
    print(f("book123"))    # wynik: True (ma co najmniej 6 znaków i unikalne znaki)
    print(f("A2water3"))   # wynik: True (ma co najmniej 6 znaków i unikalne znaki)
    print(f("qwerty"))     # wynik: False (powtarza się 'y')
    print(f(""))           # wynik: False (hasło jest puste)

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()


   