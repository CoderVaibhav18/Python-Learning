# The dir() method
# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. Example:

x = [1, 2, 3]
print(x.__len__())

# The __dict__ attribute
# __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p = Person("John", 30)
print(p.__dict__)


# The help() mehthod
# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. Example:

help(str)
