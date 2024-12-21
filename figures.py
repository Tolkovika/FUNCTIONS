import turtle

def draw_square(length):
    """Rysuje kwadrat o podanej długości boku."""
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    """Rysuje trójkąt równoboczny o podanej długości boku."""
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

def draw_rectangle(length_a, length_b):
    """Rysuje prostokąt o bokach length_a i length_b."""
    for _ in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)