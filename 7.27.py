def f(product_code: str) -> bool:
    
    if len(product_code) == 4 and product_code.isdigit():
        first_three_digits = product_code[:3]
        control_digit = int(product_code[3])
        sum_of_digits = sum(int(digit) for digit in first_three_digits)
        remainder = sum_of_digits % 7
        return remainder == control_digit
    return False


print(f("1082"))  
print(f("2035"))  
print(f("1114"))  
print(f("7071"))  
