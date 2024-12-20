def cm_to_inches(cm: float) -> float:
    """Konwertuje centymetry na cale"""
    return cm * 0.393701  #mnożymy liczbę centymetrów przez współczynnik konwersji

def feet_inch_to_cm(feet: int, inches: int) -> float:
    """Konwertuje stopy i cale na centymetry"""
    total_inches = feet * 12 + inches  #przemieniamy stopy na cale i dodajemy cale
    return total_inches * 2.54  #mnożymy liczbę cali przez 2.54, aby uzyskać wynik w centymetrach
