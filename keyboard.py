# keyboard.py

def input_string(message):
    return input(message)

def input_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer.")

def input_real(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid real number.")

def input_boolean(message):
    while True:
        choice = input(message).lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' for Yes or 'n' for No.")
