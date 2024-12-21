from range_checker import is_in_range

def main():
    try:
        number = int(input("A number: "))
        x = int(input("Enter the lower bound of the range: "))
        y = int(input("Enter the upper bound of the range: "))

        in_range = is_in_range(number, x, y)
        result = "yes" if in_range else "no"

        print(f"Number {number} in the range ({x},{y}): {result}")
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()
