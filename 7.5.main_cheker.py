from range_checker import is_in_range

number = int(input("A number: "))
x = 2
y = 15

if is_in_range(number, x, y):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")
