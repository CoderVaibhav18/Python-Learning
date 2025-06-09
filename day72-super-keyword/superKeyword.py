class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang

vaibhav = Programmer("vaibhav", "2345", "Python")
print(vaibhav.name)
print(vaibhav.id)
print(vaibhav.lang)