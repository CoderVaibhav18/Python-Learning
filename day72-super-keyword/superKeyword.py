# Super keyword in Python
# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

# Here's an example of how to use the super() keyword in a simple inheritance scenario:

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
class ChildClass(ParentClass):
    def parent_method(self):
        print("Vaibhav") 
        super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, lang):
#     super().__init__(name, id)
#     self.lang = lang

# vaibhav = Programmer("vaibhav", "2345", "Python")
# print(vaibhav.name)
# print(vaibhav.id)
# print(vaibhav.lang)