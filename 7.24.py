def f(expression: str) -> int:
    
    if all(c.isdigit() or c in '+-' for c in expression):
        return eval(expression)  # Evaluate and return the result of the expression
    else:
        raise ValueError("Invalid expression")

print(f("2+3"))        
print(f("3+8+1"))      
print(f("2+3-4+5-0"))  
