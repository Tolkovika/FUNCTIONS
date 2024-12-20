# draw_figures.py

import turtle
from figures import draw_square, draw_triangle, draw_rectangle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def move_pen(pen: turtle.Turtle, x: float, y: float):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

move_pen(pen, -150, 100)
draw_square(pen, 100)

move_pen(pen, 100, 100)
draw_square(pen, 50)

move_pen(pen, -150, -50)
draw_triangle(pen, 100)

move_pen(pen, 100, -50)
draw_triangle(pen, 50)

move_pen(pen, -150, -200)
draw_rectangle(pen, 120, 80)

move_pen(pen, 100, -200)
draw_rectangle(pen, 80, 40)

pen.hideturtle()
window.mainloop()
