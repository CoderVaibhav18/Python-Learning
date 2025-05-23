n1 = 9
n2 = 9

try:
    print("Addition of", n1, "+", n2, "is", n1 + n2)
    print("Subtraction of", n1, "-", n2, "is", n1 - n2)
    print("Multiplication of", n1, "*", n2, "is", n1 * n2)
    print("Exponential of", n1, "^", n2, "is", n1 ** n2)
    if n2 == 0:
        print("Division of", n1, "/", n2, "is Error: Division by zero")
    else:
        print("Division of", n1, "/", n2, "is", n1 / n2)
except Exception as e:
    print("An error occurred:", e)