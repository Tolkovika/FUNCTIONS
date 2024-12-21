import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)

# Rysujemy kwadrat w pierwszej lokalizacji
pen.penup()
pen.goto(-100, 100)  # Przemieszczamy żółwia do pierwszej lokalizacji
pen.pendown()
draw_square(pen, 100)  # Teraz przekazujemy 'pen' jako pierwszy argument

# Rysujemy kwadrat w drugiej lokalizacji
pen.penup()
pen.goto(100, 100)  # Przemieszczamy żółwia do drugiej lokalizacji
pen.pendown()
draw_square(pen, 100)  # Teraz przekazujemy 'pen' jako pierwszy argument

# Rysujemy trójkąt w pierwszej lokalizacji
pen.penup()
pen.goto(-100, -100)  # Przemieszczamy żółwia do pierwszej lokalizacji
pen.pendown()
draw_triangle(pen, 100)

# Rysujemy trójkąt w drugiej lokalizacji
pen.penup()
pen.goto(100, -100)  # Przemieszczamy żółwia do drugiej lokalizacji
pen.pendown()
draw_triangle(pen, 100)

# Rysujemy prostokąt w pierwszej lokalizacji
pen.penup()
pen.goto(-200, -200)  # Przemieszczamy żółwia do pierwszej lokalizacji
pen.pendown()
draw_rectangle(pen, 150, 100)

# Rysujemy prostokąt w drugiej lokalizacji
pen.penup()
pen.goto(200, -200)  # Przemieszczamy żółwia do drugiej lokalizacji
pen.pendown()
draw_rectangle(pen, 150, 100)

# Ukrywamy żółwia po skończonym rysowaniu
pen.hideturtle()
window.mainloop()