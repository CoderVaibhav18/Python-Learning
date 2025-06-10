class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
    return self.x * self.y
  
class Circle(Shape):
  def __init__(self, radius):
    super().__init__(radius, radius)
    self.radius = radius
  
  def area(self):
    return 3.14 * super().area() 
    
  
# s = Shape(3, 5)
# print(s.area())

c = Circle(5)
print(c.area())