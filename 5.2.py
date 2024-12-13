from converters import cm_to_inches, feet_inch_to_cm  # Importujemy funkcje z pliku converters.py

def test_cm_to_inches():
    """Testujemy konwersję centymetrów na cale"""
    cm_values = [1, 10, 100, 25.4]  # Różne wartości w centymetrach
    for cm in cm_values:  # Iterujemy przez wszystkie wartości centymetrów
        result = cm_to_inches(cm)  # Wywołujemy funkcję konwertującą
        print(f"{cm} cm to {result} cali")  # Wypisujemy wynik konwersji

def test_feet_inch_to_cm():
    """Testujemy konwersję stóp i cali na centymetry"""
    test_cases = [(5, 8), (6, 0), (0, 12), (3, 2)]  # Przykładowe dane wejściowe: (stopy, cale)
    for feet, inches in test_cases:  # Iterujemy przez przypadki testowe
        result = feet_inch_to_cm(feet, inches)  # Wywołujemy funkcję konwertującą
        print(f"{feet} stóp {inches} cali to {result} cm")  # Wypisujemy wynik konwersji

def main():
    """Funkcja główna uruchamiająca testy"""
    print("Testowanie konwersji cm na cale:")
    test_cm_to_inches()  # Testujemy konwersję cm na cale

    print("\nTestowanie konwersji stóp i cali na cm:")
    test_feet_inch_to_cm()  # Testujemy konwersję stóp i cali na cm

# Uruchamiamy funkcję main, jeśli skrypt jest uruchomiony bezpośrednio
if __name__ == "__main__":
    main()
