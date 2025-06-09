# class method in python
# Class ke naam se call hota hai (object ki zarurat nahi hoti)
# Uska first parameter cls hota hai, na ki self
# cls ka use karke class variables ya class ko hi modify kar sakte ho

class Employee:
  company = "Apple"
  
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")
  
  @classmethod  
  def changeCompany(cls, newCompany):
    cls.company = newCompany
    
e1 = Employee()
e1.name = "Vaibhav"
e1.show()
e1.changeCompany("Google")
e1.show()
print(Employee.company)