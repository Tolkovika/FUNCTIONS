def power(x, n):
    # Base case: x^0 = 1
    if n == 0:
        return 1
    # Recursive case: x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)

# Assign values to a and b
a = 5
b = 3

# Call the power function using a and b
result = power(a, b)

# Print the result
print(f"{a}^{b} = {result}")
