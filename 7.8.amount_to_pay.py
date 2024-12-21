def f(amount_to_pay: int) -> int: #amount_to_pay całkowita kwota do zapłaty int zwraca min  liczbe monet do zaplaty
    
    # sprawdzenie, czy kwota jest nieujemna
    if amount_to_pay < 0:
        raise ValueError("Kwota do zapłaty musi być liczbą całkowitą nieujemną.")

    # dostępne nominały monet w porządku malejącym
    coins = [5, 2, 1]
    num_coins = 0

    # obliczanie minimalnej liczby monet
    for coin in coins:
        num_coins += amount_to_pay // coin  
        amount_to_pay %= coin  # aktualizujemy pozostałą kwotę do zapłaty

    return num_coins

def main():
    print(f(23))  #  6 
    print(f(8))   #  3 
    print(f(2))   #  1 
    print(f(0))   #  0 

# warunek uruchamiania programu
if __name__ == "__main__":
    main()
