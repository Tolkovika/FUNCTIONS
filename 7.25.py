def f(x: int, y: int) -> int:
    
    total_sum = 0
    for number in range(x, y + 1):
        if number % 6 == 0 and number % 4 != 0:
            total_sum += number
    return total_sum

print(f(1, 20))   
print(f(10, 30))  

