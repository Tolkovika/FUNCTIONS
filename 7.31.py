def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

a = 5
b = 3

result = power(a, b)
print(f"{a}^{b} = {result}")