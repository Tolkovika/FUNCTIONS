def f(detector: str) -> bool:
    """
    Zwraca True, jeśli przynajmniej 3 osoby były jednocześnie w pokoju, w przeciwnym razie False.

    Argumenty:
        detector (str): Ciąg znaków reprezentujący wejścia ('+') i wyjścia ('-') z pokoju.

    Zwraca:
        bool: True, jeśli przynajmniej 3 osoby były jednocześnie w pokoju, False w przeciwnym razie.
    """
    count = 0  # licznik osób w pokoju
    for event in detector:
        if event == '+':  # jeśli ktoś wchodzi, zwiększamy licznik
            count += 1
        elif event == '-':  # jeśli ktoś wychodzi, zmniejszamy licznik
            count -= 1

        # sprawdzamy, czy w pokoju jest co najmniej 3 osoby
        if count >= 3:
            return True
    
    # jeśli warunek nie został spełniony, zwróć False
    return False

def main():
    print(f("+-+++-+---"))  # wynik: True
    print(f("+-+-+-+-"))    # wynik: False
    print(f("+-++-+--"))    # wynik: False
    print(f("+-++-++-+---")) # wynik: True

if __name__ == "__main__":
    main()
