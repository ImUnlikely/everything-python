# the * sign

x = 10
y = 5

z = x * y # 50
print(z)


x = 10
y = -5

z = x * y # -50
print(z)


# strings
str1 = "Hello!"
str2 = "What?"

mystring = str1*5
print(mystring)

mystring = str1 + " " * 5 # Hello! with long space
print(mystring)

mystring = (str1 + " ") * 5 # Hello! with space, five times
print(mystring)

mystring = str2 * 5 + str(x * y) # remember order of operations
print(mystring)


# lists
alist = [5]

mylist = alist * 5 # [5, 5, 5, 5, 5]
print(mylist)

alist = [5, 6]
mylist = alist * 5 # [5, 6, 5, 6, 5, 6, 5, 6, 5, 6]
print(mylist)

mylist = [x*5 for x in alist] # perform multiplication for all elements in a list
print(mylist)


alist = ["Hello", "What", 5]

mylist = alist * 3 # ['Hello', 'What', 5, 'Hello', 'What', 5, 'Hello', 'What', 5]
print(mylist)


# Nested lists

mylist = [[x] for x in alist] # [['Hello'], ['What'], [5]]
print(mylist)

mylist = [alist*2 for x in range(2)] # [['Hello', 'What', 5, 'Hello', 'What', 5], ['Hello', 'What', 5, 'Hello', 'What', 5]]
print(mylist)

mylist = [alist[x]*3 for x in range(alist.__len__())] # ['HelloHelloHello', 'WhatWhatWhat', 15]
print(mylist)