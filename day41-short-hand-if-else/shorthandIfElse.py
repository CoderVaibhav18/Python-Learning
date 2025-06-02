a = 45
b = 45
print(f"{a} is bigger") if a > b else print("a & b is euqal") if a == b else print(f"{b} is bigger") 

a = 42
b = 45
c = a if a > b else "a & b is euqal" if a == b else b

print(f"Your number {c} is bigger")