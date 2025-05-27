
# Argument : Required Argument, Default Argument, keyword Argument
# def avg(a, b=3):
#   avg = (a+b)/2
#   print("The avg is:", avg)
  
# avg(b=9,a=5)


# tuple
# def average(*numbers):
#   print(type(numbers))
#   sum = 0
#   for i in numbers:
#     sum += i
#   return sum/len(numbers)

# a = average(3, 7, 8)
# print(a)

# dictionary
def name(**names):
  print(type(names))
  print("Hello", names['fname'], names['lname'])
  
name(fname="Vaibhav", lname="Sathe")