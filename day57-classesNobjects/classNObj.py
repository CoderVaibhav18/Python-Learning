# class & object - A class is a blueprin or a template of an object
# self - wo object jiske liye method call ho rha hai

class Person:
  name = "Vaibhav"
  occupation = "student"
  networth = 20
  def info(self):
    print(f"{self.name} is a {self.occupation}")
  
  
a = Person()
b = Person()

a.name = "DM"
a.occupation = "HR"
a.info()

b.name = "Virat"
b.occupation = "Cricketer"
b.info()
