def func1():
  try:
    l = [2, 3, 4, 5, 57]
    a = int(input("Enter a index:"))
    print(l[a])
    return 1
  except:
    print("Some error occured")
    return 0
  finally:
    print("Im always executed")
    
c = func1()
print(c)