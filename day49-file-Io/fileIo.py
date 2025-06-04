# Extract - reading a file
f = open('hello.txt', 'r')
text = f.read()
print(text)
f.close()

# Writing a file
f = open('hello.txt', 'w')
f.write("Hello world!!")
f.close()

# Append a file
f = open('hello.txt', 'a')
f.write(" from vaibhav")
f.close()