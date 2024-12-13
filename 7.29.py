def factorial(n):
    # jeśli n to 0 lub 1, zwracamy 1 (silnia 0 i 1 wynosi 1)
    if n == 0 or n == 1:
        return 1

    # jeśli n > 1, obliczamy silnię rekurencyjnie
    if n > 1:
        return n * factorial(n - 1)

def main():
    # testowanie funkcji silnia dla liczby 5
    n = 5
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

# Uruchamiamy funkcję main, jeśli skrypt jest uruchamiany jako główny
if __name__ == "__main__":
    main()
