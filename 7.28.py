def f(dice: str) -> int:
    """
    Zwraca długość najdłuższej sekwencji powtarzających się cyfr w ciągu rzutów kością.

    Argumenty:
        dice (str): Ciąg reprezentujący rzuty kością.

    Zwraca:
        int: Długość najdłuższej sekwencji powtarzających się cyfr.
    """
    max_streak = 1  # inicjujemy zmienną do przechowywania maksymalnej sekwencji
    current_streak = 1  # inicjujemy zmienną do przechowywania bieżącej sekwencji

    # iterujemy przez wszystkie cyfry w ciągu
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  # jeśli bieżąca cyfra jest taka sama jak poprzednia
            current_streak += 1  # zwiększamy długość bieżącej sekwencji
        else:
            current_streak = 1  # jeśli cyfra jest inna, resetujemy bieżącą sekwencję

        # ustawiamy maksymalną sekwencję na większą z bieżącej i maksymalnej sekwencji
        max_streak = max(max_streak, current_streak)

    return max_streak  # zwracamy długość najdłuższej sekwencji powtarzających się cyfr

def main():
    print(f("5233165554211"))  
    print(f("2133"))          
    print(f("1234"))           
    print(f("77777"))          

if __name__ == "__main__":
    main()