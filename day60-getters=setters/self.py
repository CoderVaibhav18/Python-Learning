class Person:
  
  def __init__(self, name, age):
    self.name = name
    self._age = age
    
  # Getter for age
  @property
  def age(self):
    print("Getter for age")
    return self._age
  
  # Setter for age
  @age.setter
  def age(self, age):
    print("setter for age")
    self._age = age
    
  @property
  def next_birthday(self):
    return self._age + 1
      
a = Person("Vaibhav", 20)

# Access age (uses getter)
print(a.age) # Output: Getting age... 20

# Update age (uses setter)
a.age = 21 # Output: Setting age...
print(a.age) # Output: Getting age... 21

