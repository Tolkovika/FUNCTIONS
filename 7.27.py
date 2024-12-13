def f(product_code: str) -> bool:
    """
    Sprawdza, czy kod produktu jest prawidłowy zgodnie z określoną metodą weryfikacji.

    Argumenty:
        product_code (str): Kod produktu, który ma być sprawdzony.

    Zwraca:
        bool: Zwraca True, jeśli kod produktu jest prawidłowy, w przeciwnym razie False.
    """
    # sprawdzamy, czy kod produktu ma długość 4 i składa się wyłącznie z cyfr
    if len(product_code) == 4 and product_code.isdigit():
        first_three_digits = product_code[:3] #pierwsze 3
        control_digit = int(product_code[3]) #czwórka kontrolna (ostatnia cyfra)
        sum_of_digits = sum(int(digit) for digit in first_three_digits) #obliczamy sumę pierwszych trzech cyfr
        remainder = sum_of_digits % 7 #obliczamy resztę z dzielenia sumy cyfr przez 7
        return remainder == control_digit #porównujemy resztę z czwórką kontrolną
    # jeśli kod nie spełnia warunków, zwracamy False
    return False

def main():
    print(f("1082"))  # wynik: True, ponieważ 1+0+8 = 9, 9 % 7 = 2 
    print(f("2035"))  # wynik: False
    print(f("1114"))  # wynik: True, ponieważ 1+1+1 = 3, 3 % 7 = 3 
    print(f("7071"))  # wynik: False

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()


