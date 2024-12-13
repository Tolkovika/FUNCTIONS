# draw_figures.py

import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")  # Ustawiamy tło na zielone

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)  # Ustawiamy prędkość rysowania

# Rysowanie kwadratu w pierwszej lokalizacji
pen.penup()  # Podnosimy pióro, aby żółw się przemieszczał bez rysowania
pen.goto(-100, 100)  # Przemieszczamy żółwia do nowego miejsca
pen.pendown()  # Kładziemy pióro, aby zaczynać rysować
draw_square(100)  # Rysujemy kwadrat o boku 100

# Rysowanie kwadratu w drugiej lokalizacji
pen.penup()
pen.goto(100, 100)  # Nowa lokalizacja
pen.pendown()
draw_square(100)  # Rysujemy drugi kwadrat

# Rysowanie trójkąta w pierwszej lokalizacji
pen.penup()
pen.goto(-100, -50)  # Nowa lokalizacja
pen.pendown()
draw_triangle(100)  # Rysujemy trójkąt

# Rysowanie trójkąta w drugiej lokalizacji
pen.penup()
pen.goto(100, -50)  # Nowa lokalizacja
pen.pendown()
draw_triangle(100)  # Rysujemy drugi trójkąt

# Rysowanie prostokąta w pierwszej lokalizacji
pen.penup()
pen.goto(-100, -200)  # Nowa lokalizacja
pen.pendown()
draw_rectangle(150, 80)  # Rysujemy prostokąt o bokach 150 i 80

# Rysowanie prostokąta w drugiej lokalizacji
pen.penup()
pen.goto(100, -200)  # Nowa lokalizacja
pen.pendown()
draw_rectangle(150, 80)  # Rysujemy drugi prostokąt

# Ukrywamy żółwia i kończymy
pen.hideturtle()
window.mainloop()  # Uruchamiamy główną pętlę programu, aby okno pozostało otwarte
