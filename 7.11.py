def f(n1: int, n2: int, n3: int) -> bool:  #bool True, jeśli przynajmniej jedna liczba jest ujemna, False w przeciwnym razie

    # sprawdzamy czy któraś z liczb jest ujemna
    return n1 < 0 or n2 < 0 or n3 < 0

def main():
    print(f(11, 6, -4))  
    print(f(5, 4, 14))   
    print(f(-1, 0, 3))   
    print(f(0, 0, 0))    
    print(f(-5, -2, -8)) 

#  uruchamiamy skrypt bezpośrednio, to wywołujemy main()
if __name__ == "__main__":
    main()