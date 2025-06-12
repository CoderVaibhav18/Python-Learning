class Person:
  def show(self):
    print("Im a Person")

class Student(Person):
  def study(self):
    print("Im studying")

class Employee(Person):
  def work(self):
    print("Im working")

class PartTimeStudent(Student, Employee):
  def details(self):
    print("I am a part-time student and employee.")
    
p = PartTimeStudent()
p.show()
p.study()
p.work()
p.details()