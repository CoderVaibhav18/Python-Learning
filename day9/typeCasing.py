# Type Casting in python is converting onr data type into other is known as type casting
"""
Python supports a wide variety of functions or methods like: int(), float(), stro, ordo, hex(), oct), tuple(), set(), list), dict), etc. for the type casting in python.

Two Types of Typecasting:

1. Explicit Conversion (Explicit type casting in python)
2. Implicit Conversion (Implicit type casting in python).
"""

# Explicit Conversion - progammer try to change their data type
a = "1" # throw the error if string is not valid string
b = "2"
print(int(a) + int(b))

# Implicit conversion - python automatically converts the lower data type into higher data type
c = 8.9
d = 9
print(c+d) 
print(type(c))
print(type(d))
