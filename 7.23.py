def f(password: str) -> bool:
    
    if len(password) >= 6 and len(set(password)) == len(password):
        return True
    return False

print(f("ax15"))       
print(f("book123"))    
print(f("A2water3"))   
print(f("qwerty"))     
print(f(""))           