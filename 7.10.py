def f(x: int, y: int) -> int:  #x początek zakresu y koniec zakresu ,zwraca liczbe ujemnych liczb parzystych w zakresie

    # tworzymy listę liczb w zakresie od x do y i filtrujemy te, które są ujemne i parzyste
    return len([num for num in range(x, y) if num < 0 and num % 2 == 0])

def main():
    # Testujemy funkcję f() dla różnych zakresów
    print(f(-7, 8))    # wynik: 3 (-6, -4, -2)
    print(f(-1, 11))   #  wynik: 0 (brak liczb ujemnych w zakresie)
    print(f(-10, -1))  # wynik: 5 (-10, -8, -6, -4, -2)
    print(f(-15, -10)) #  wynik: 3 (-14, -12, -10)
    print(f(0, 10))    #  wynik: 0 (brak liczb ujemnych)

# Jeśli uruchamiamy skrypt bezpośrednio, to wywołujemy main()
if __name__ == "__main__":
    main()