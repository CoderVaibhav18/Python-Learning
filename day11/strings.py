# String is basically anything that you enclose between the single or double quotation is considered as strings
name = 'Vaibhav'
friend = 'Pratisha'
print(name, friend)

chats = """
hello, im vaibhav
Hey, im good
"I want eat an apple.
"""
print(chats)

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7]) # throw error string index out of range

for name in chats:
  print(name)