info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

for value in info.values():
  print(value)

for key in info.keys():
  print(f" {key} : {info[key]}")

print(info.items())

for key, value in info.items():
  print(f"{key} is {value}") 
  