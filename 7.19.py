from collections import Counter

def f(number: int) -> int:
    """
    Zwraca sumę powtarzających się cyfr w danej liczbie.

    Argumenty:
        number (int): Liczba, w której mają zostać znalezione powtarzające się cyfry.

    Zwraca:
        int: Suma powtarzających się cyfr.
    """
    # Konwertujemy liczbę na ciąg znaków, aby łatwiej przejść przez jej cyfry
    str_number = str(number)

    # Liczymy, ile razy każda cyfra występuje
    digit_count = Counter(str_number)

    # Obliczamy sumę powtarzających się cyfr (czyli tych, które występują więcej niż raz)
    sum_repeated_digits = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)

    return sum_repeated_digits

def main():
    print(f(1027))        # wynik: 0 (brak powtarzających się cyfr)
    print(f(230335))      # wynik: 9 (3 + 3 + 3)
    print(f(513553007))   # wynik: 21 (5 + 5 + 3 + 3 + 0 + 0)

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()




