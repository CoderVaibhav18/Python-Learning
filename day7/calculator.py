num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))

operator = input("Enter ur choice: ")

ans = 0
operation = ''


if operator == '+':
  ans = num1 + num2
  operation = 'Addition'
elif operator == '-':
  ans = num1 - num2
  operation = 'Substraction'
elif operator == '*':
  ans = num1 * num2
  operation = 'Multiplication'
elif operator == '/':
  ans = num1 / num2
  operation = 'Division'
elif operator == '^':
  ans = num1 ** num2
  operation = 'Square'
else:
  print('Plz enter a valid operator')
  
print(operation, "of", num1, "", operator, num2, "is", ans)
