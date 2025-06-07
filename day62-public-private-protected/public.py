
# Public Access Specifier - All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

class Person:
  def __init__(self, name):
    self.name = name
    
q = Person("vaibhav")
print(q.name)