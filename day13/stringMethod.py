# Python provides a set of built-in methods that we can use to alter and modify the strings.

# Upper()
name = "Vaibhav"
print(name.upper())


# Lower()
name = "Vaibhav"
print(name.lower())

# strip : removes any white spaces before and after string
name = " Vaibhav Sathe "
print(name.strip())

# rstrip() : removes any trailing characters.
name = "!!!Vaibhav!!!"
print(name.rstrip("!"))
print(len(name.rstrip("!")))

# replace() : replace all occurence of the string with another string
str1 = "JPython"
print(str1.replace("J", "C"))

# split() : split gives string at specific instance and returns strings as list items.
str1 = "python java js"
print(str1.split(" "))

# capitalize() : Turns 1st character to upper and rest of the charcter into lowercase
str = "Vaibhav sathE"
print(str.capitalize())

# center() : The center() method aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50, "-"))

# count() : The count() method returns the number of times the given value has occurred within the given string.
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

# endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# find() : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

str = "Vaibhav"
print(str.find("k"))

# index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# str = "Vaibhav"
# print(str.index("k"))

# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str = "Wlcomtoyputube"
print(str.isalnum())

# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())

# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "hello world"
print(str1.islower())

# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
# Example:
str1 = "      "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# Example:
str1 = "World Health Organization" 
print(str1.istitle())

# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

# startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
# Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
# Example:
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# title() :
# The title() method capitalizes each letter of the word within the string.
# Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())