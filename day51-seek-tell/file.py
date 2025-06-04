# with open('file.txt', 'r') as f:
#   f.seek(18)
#   print(f.tell())
#   data = f.read(4)
#   print(data)

with open('file.txt', 'w') as f:
  f.write('vaibhav sathe')
  f.truncate(7)

with open('file.txt', 'r') as f:
  print(f.read())