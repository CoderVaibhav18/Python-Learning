# marks = [34, 56, 78, 98, 90, 77, 99, 56]
# index = 0
# for mark in marks:
#   print(mark)
#   if index == 3:
#     print(f"Congrats Vaibhav!! You score good marks i.e., {marks[index]}")
#   index += 1

marks = [34, 56, 78, 98, 90, 77, 99, 56]
for index, mark in enumerate(marks, start=1):
  print(mark)
  if index == 3:
    print(f"Congrats Vaibhav!! You score good marks i.e., {marks[index]}")
