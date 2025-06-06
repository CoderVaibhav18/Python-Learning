# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Pyth

class Person:
  def __init__(self, name, occ):
    print("Hey, im constructor")
    self.name = name
    self.occ = occ
    
  def info(self):
    print(f"{self.name} is a {self.occ}")
  
a = Person("Vaibhav", "Software Developer")
a.info()