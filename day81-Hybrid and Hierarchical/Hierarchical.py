class Animal:
  def breathe(self):
    print("Breathe....")
    
class Dog(Animal):
  def bark(self):
    print("Barking....")
    
class Cat(Animal):
  def meow(self):
    print("meowing....")
    
class Cow(Animal):
  def moo(self):
    print("Mooing....")
    
d = Dog()
d.breathe()
d.bark()

c = Cat()
c.breathe()
c.meow()

cc = Cow()
cc.breathe()
cc.moo()