# Operator Overloading in Python: An Introduction
# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

class Vector:
  
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k
    
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
  def __add__(self, other):
    return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
  
  def __sub__(self, other):
    return Vector(self.i - other.i, self.j - other.j, self.k - other.k)
  
  def __mul__(self, other):
    return Vector(self.i * other.i, self.j * other.j, self.k * other.k)
  
v1 = Vector(3, 4, 6)
print(v1)
v2 = Vector(2, 3, 5)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2