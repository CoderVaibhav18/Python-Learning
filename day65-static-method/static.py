# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
# result = Math.add(1, 2)
# print(result) # Output: 3

# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.

class Math:
  def __init__(self, num):
    self.num = num
    
  def add_nums(self, n):
    self.num = self.num + n
    
  @staticmethod
  def add(a, b):
    return a + b
    
a = Math(12)
print(a.num)
a.add_nums(2)
print(a.num)
print(Math.add(1,2))