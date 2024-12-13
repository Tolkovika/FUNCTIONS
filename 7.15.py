def f(detector: str) -> bool:
    """
    Zwraca True, jeśli przynajmniej 3 osoby były jednocześnie w pokoju, w przeciwnym razie False.

    Argumenty:
        detector (str): Ciąg znaków reprezentujący wejścia ('+') i wyjścia ('-') z pokoju.

    Zwraca:
        bool: True, jeśli przynajmniej 3 osoby były jednocześnie w pokoju, False w przeciwnym razie.
    """
    count = 0  # Licznik osób w pokoju
    for event in detector:
        if event == '+':  # Jeśli ktoś wchodzi, zwiększamy licznik
            count += 1
        elif event == '-':  # Jeśli ktoś wychodzi, zmniejszamy licznik
            count -= 1

        # Sprawdzamy, czy w pokoju jest co najmniej 3 osoby
        if count >= 3:
            return True

    # Jeśli nigdy nie było 3 osób jednocześnie, zwracamy False
    return False

def main():
    print(f("+-+++-+---"))  # wynik: True
    print(f("+-+-+-+-"))    # wynik: False
    print(f("+-++-+--"))    # wynik: False
    print(f("+-++-++-+---")) # wynik: True

# Sprawdzamy, czy uruchamiamy plik jako główny skrypt
if __name__ == "__main__":
    main()
