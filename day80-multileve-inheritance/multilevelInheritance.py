# Multilevel Inheritance in Python
# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.

# In Python, multilevel inheritance is achieved by using the class hierarchy. The syntax for multilevel inheritance is quite simple and follows the same syntax as single inheritance.

# Syntax
# class BaseClass:
#     # Base class code
    
# class DerivedClass1(BaseClass):
#     # Derived class 1 code
    
# class DerivedClass2(DerivedClass1):
#     # Derived class 2 code
# In the above example, we have three classes: BaseClass, DerivedClass1, and DerivedClass2. The DerivedClass1 class inherits from the BaseClass, and the DerivedClass2 class inherits from the DerivedClass1 class. This creates a hierarchy where DerivedClass2 has access to all the attributes and methods of both DerivedClass1 and BaseClass.



class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    
  def show(self):
    print(f"Name: {self.name}")
    print(f"Species: {self.species}")
    
class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed
  
  def show(self):
    Animal.show(self)
    print(f"Breed: {self.breed}")
    
class GoldenRetriever(Dog):
  def __init__(self, name, color):
    Dog.__init__(self, name, breed="Golden Retriever")
    self.color = color
    
  def show(self):
    Dog.show(self)
    print(f"Color: {self.color}")
    
a = GoldenRetriever("Tommy", "black")
a.show()