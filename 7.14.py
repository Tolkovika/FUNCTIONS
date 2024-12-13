def f(number1: float, number2: float, operator: str) -> float:
    """
    Wykonuje operację arytmetyczną na dwóch liczbach w oparciu o podany operator.

    Argumenty:
        number1 (float): Pierwsza liczba.
        number2 (float): Druga liczba.
        operator (str): Operator arytmetyczny (+, -, *, %, **).

    Zwraca:
        float: Wynik operacji arytmetycznej.
    """
    # Dodawanie
    if operator == "+":
        return number1 + number2
    # Odejmowanie
    elif operator == "-":
        return number1 - number2
    # Mnożenie
    elif operator == "*":
        return number1 * number2
    # Modulo (reszta z dzielenia)
    elif operator == "%":
        return number1 % number2
    # Potęgowanie
    elif operator == "**":
        return number1 ** number2
    # Obsługa nieobsługiwanego operatora
    else:
        raise ValueError("Nieobsługiwany operator. Użyj jednego z +, -, *, %, **.")

def main():
    print(f(2, 3, "+"))   # wynik: 5
    print(f(2, 3, "%"))   # wynik: 2
    print(f(2, 3, "**"))  # wynik: 8
    print(f(2, 3, "*"))   # wynik: 6
    print(f(2, 3, "-"))   # wynik: -1

# Sprawdzamy, czy uruchamiamy plik jako główny skrypt
if __name__ == "__main__":
    main()
