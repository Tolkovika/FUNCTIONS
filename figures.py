import turtle

def draw_square(pen: turtle.Turtle, length: float):
    """Rysuje kwadrat o podanej długości boku."""
    for _ in range(4):
        pen.forward(length)  # Rysowanie boku
        pen.right(90)        # Obrót o 90 stopni w prawo

def draw_triangle(pen: turtle.Turtle, length: float):
    """Rysuje trójkąt równoramienny o podanej długości boku."""
    for _ in range(3):
        pen.forward(length)  # Rysowanie boku
        pen.left(120)        # Obrót o 120 stopni w lewo

def draw_rectangle(pen: turtle.Turtle, length_a: float, length_b: float):
    """Rysuje prostokąt o podanych długościach boków a i b."""
    for _ in range(2):
        pen.forward(length_a)  # Dłuższy bok
        pen.right(90)          # Obrót o 90 stopni w prawo
        pen.forward(length_b)  # Krótszy bok
        pen.right(90)          # Obrót o 90 stopni w prawo

