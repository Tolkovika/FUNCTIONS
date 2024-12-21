from collections import Counter   #zwraca sumę powtarzających się cyfr w danej liczbie i liczy sume potarz

def f(number: int) -> int:
    str_number = str(number)   # konwertujemy liczbę na ciąg znaków aby łatwiej przejść przez jej cyfry

    digit_count = Counter(str_number)   #liczymy ile razy każda cyfra występuje

    # obliczamy sumę powtarzających się cyfr 
    sum_repeated_digits = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)

    return sum_repeated_digits

def main():
    print(f(1027))        
    print(f(230335))      
    print(f(513553007))   

if __name__ == "__main__":
    main()



