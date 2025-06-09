# class method in python
# Class ke naam se call hota hai (object ki zarurat nahi hoti)
# Uska first parameter cls hota hai, na ki self
# cls ka use karke class variables ya class ko hi modify kar sakte ho

# Conclusion
# Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.

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