x = 8
match x:
  case 0:
    print("zero")
  case 1: 
    print("one")
  case _ if x != 8:
    print("def")
  case _ if x != 9:
    print("def2")