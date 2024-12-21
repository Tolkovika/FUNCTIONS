def f(expression: str) -> int:
    """
    Zwraca wynik obliczenia wyrażenia matematycznego.

    Argumenty:
        expression (str): Wyrażenie matematyczne, które ma zostać obliczone.

    Zwraca:
        int: Wynik obliczenia wyrażenia matematycznego.

    Podnosi:
        ValueError: Jeśli wyrażenie zawiera niepoprawne znaki.
    """
    # sprawdzamy, czy wszystkie znaki w wyrażeniu są cyframi lub operatorami +, -
    if all(c.isdigit() or c in '+-' for c in expression):
        return eval(expression)  # oblicz i zwróć wynik wyrażenia
    else:
        raise ValueError("Invalid expression")  # jesli wyrażenie zawiera niepoprawne znaki zgłaszamy błąd

def main():
    print(f("2+3"))        # wynik: 5
    print(f("3+8+1"))      # wynik: 12
    print(f("2+3-4+5-0"))  # wynik: 6

if __name__ == "__main__":
    main()