def power(x, n):
    # jeśli n to 0, zwracamy 1, ponieważ każda liczba do potęgi 0 to 1
    if n == 0:
        return 1
    else:
        #obliczamy potęgowanie: x^n = x * x^(n-1)
        return x * power(x, n - 1)

def main():
    a = 5  # Podstawa
    b = 3  # Wykładnik

    # obliczamy potęgę a^b
    result = power(a, b)
    print(f"{a}^{b} = {result}")

# Uruchamiamy funkcję main, jeśli skrypt jest uruchamiany jako główny
if __name__ == "__main__":
    main()