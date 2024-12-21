from converters import cm_to_inches, feet_inch_to_cm  # Import wymaganych funkcji

def test_cm_to_inches():
    """Test konwersji cm na cale"""
    cm_values = [1, 10, 100, 25.4]  # Dane testowe w cm
    for cm in cm_values:
        result = cm_to_inches(cm)
        print(f"{cm} cm to {result} cali")

def test_feet_inch_to_cm():
    """Test konwersji stóp i cali na cm"""
    test_cases = [(5, 8), (6, 0), (0, 12), (3, 2)]  # Dane testowe: (stopy, cale)
    for feet, inches in test_cases:
        result = feet_inch_to_cm(feet, inches)
        print(f"{feet} stóp {inches} cali to {result} cm")

def main():
    print("Testowanie konwersji cm na cale:")
    test_cm_to_inches()

    print("\nTestowanie konwersji stóp i cali na cm:")
    test_feet_inch_to_cm()

if __name__ == "__main__":
    main()
