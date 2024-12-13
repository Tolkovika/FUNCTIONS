def f(x: int, y: int) -> int:
    """
    Zwraca sumę liczb w zakresie od x do y (w tym), które są podzielne przez 6, ale nie są podzielne przez 4.

    Argumenty:
        x (int): Początek zakresu.
        y (int): Koniec zakresu.

    Zwraca:
        int: Suma liczb spełniających warunki.
    """
    total_sum = 0  #zmienna do przechowywania sumy
    #iterujemy po liczbach w zakresie od x do y (w tym)
    for number in range(x, y + 1):
        #sprawdzamy, czy liczba jest podzielna przez 6, ale nie przez 4
        if number % 6 == 0 and number % 4 != 0:
            total_sum += number  # dodajemy liczbę do sumy
    return total_sum  # Zwracamy obliczoną sumę

def main():
    print(f(1, 20))   #wynik: 30 (6 + 18)
    print(f(10, 30))  #wynik: 48 (18 + 30)

# Sprawdzamy, czy skrypt jest uruchamiany jako główny program
if __name__ == "__main__":
    main()
