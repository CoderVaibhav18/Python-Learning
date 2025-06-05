# Map method in python

# def square(x):
#   return x*x

# l = [1, 2, 3, 4, 5, 6]
# newl = []
# for i in l:
#   newl.append(square(i))
# print(newl)

# lis = list(map(lambda x: x*x*x, l))
# print(lis)

# # FILTER
# l = [1, 2, 3, 4, 5, 6]

# def filterfunc(a):
#   return a>4

# l1 = list(filter(filterfunc, l))
# print(l1)

# REDUCE
from functools import reduce
l = [1, 2, 3, 4, 5, 6]

sum = reduce(lambda x, y: x+y, l)
print(sum)
