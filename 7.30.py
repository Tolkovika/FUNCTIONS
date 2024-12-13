def sum_natural(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: sum of numbers from 1 to n
    else:
        return n + sum_natural(n - 1)

# Calculate the sum of natural numbers from 1 to 10
result = sum_natural(10)
print(f"The sum of natural numbers from 1 to 10 is {result}")
