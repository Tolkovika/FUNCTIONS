def f(text: str) -> str:
    
    return '-'.join(text) if text else ""

print(f("University"))  
print(f("UE"))          
print(f("x"))           
print(f("")) 