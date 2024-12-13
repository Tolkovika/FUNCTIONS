def sum_natural(n):
    # jeśli n to 1, zwracamy 1, ponieważ suma liczb naturalnych do 1 to 1
    if n == 1:
        return 1
    else:
        #obliczamy sumę liczb naturalnych od 1 do n
        return n + sum_natural(n - 1)

def main():
    #obliczamy sumę liczb naturalnych od 1 do 10
    result = sum_natural(10)
    print(f"The sum of natural numbers from 1 to 10 is {result}")

# Uruchamiamy funkcję main, jeśli skrypt jest uruchamiany jako główny
if __name__ == "__main__":
    main()