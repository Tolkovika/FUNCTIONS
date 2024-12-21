import math
def triangle_area(a, b, c):
    """
    funkcja oblicza pole trójkąta na podstawie długości jego boków
    za pomocą wzoru Herona.

    argumenty:
    a (float): Długość pierwszego boku trójkąta
    b (float): Długość drugiego boku trójkąta
    c (float): Długość trzeciego boku trójkąta

    Zwraca:
    float: Pole trójkąta
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a1, b1, c1 = 3, 4, 5
area1 = triangle_area(a1, b1, c1)
print(f"The area of a triangle with sides {a1}, {b1}, and {c1} is {area1}")

a2, b2, c2 = 5, 12, 13
area2 = triangle_area(a2, b2, c2)
print(f"The area of a triangle with sides {a2}, {b2}, and {c2} is {area2}")

a3, b3, c3 = 7, 24, 25
area3 = triangle_area(a3, b3, c3)
print(f"The area of a triangle with sides {a3}, {b3}, and {c3} is {area3}")