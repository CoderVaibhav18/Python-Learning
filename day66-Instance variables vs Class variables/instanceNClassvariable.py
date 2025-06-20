# Class variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

# class MyClass:
#     class_variable = 0
    
#     def __init__(self):
#         MyClass.class_variable += 1
        
#     def print_class_variable(self):
#         print(MyClass.class_variable)
        
# obj1 = MyClass()
# obj1.print_class_variable() # Output: 1
# obj2 = MyClass()
# obj2.print_class_variable() # Output: 2

# Instance Variables
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.

# class MyClass:
#     def __init__(self, name):
#         self.name = name
        
#     def print_name(self):
#         print(self.name)
# obj1 = MyClass("John")
# obj2 = MyClass("Jane")
# obj1.print_name() # Output: John
# obj2.print_name() # Output: Jane

# In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.

class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees += 1
  def showDetails(self):
    print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")
    
emp1 = Employee("Vaibhav")
emp1.showDetails()
print(Employee.companyName)
Employee.companyName = "Google"
emp2 = Employee("Pratisha")
emp2.raise_amount = 0.2
emp2.showDetails()

# Employee.showDetails(emp1)