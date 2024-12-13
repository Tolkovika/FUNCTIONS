def sum_digits(any_number):
    return sum(int(digit) for digit in str(any_number))

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
