class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    
  def sound(self):
    print("Sound made by the animal")
    
class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="dog")
    self.breed = breed
    
  def sound(self):
    print("Bark!")
    
d = Dog("dog", "dogman")
d.sound()

a = Animal("dog", "dog")
a.sound()
    