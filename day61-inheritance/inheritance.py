class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id
    
  def showDetails(self):
    print(f"The name of employee: {self.id} is {self.name}")
    
class Programmer(Employee):
  def showprogramer(self):
    print("This is a programmer")
    
a = Employee("Vaibhav", 1)
a.showDetails()

b = Programmer("Dm", 12)
b.showDetails()
b.showprogramer()
