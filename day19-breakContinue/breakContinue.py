# n = int(input("Enter any number: "))
# for i in range(1, 13):
#   print(n, "X", i, "=", n * i)
#   if i == 10:
#     break
  
# n = int(input("Enter any number: "))
# for i in range(1, 13):
#   if i == 10:
#     print("skip the itaration")
#     continue
#   print(n, "X", i, "=", n * i)

i = 1
while True:
  print(i)
  i += 1
  if i % 101 == 0:
    break