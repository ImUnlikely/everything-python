nums = [x for x in range(0,11)]
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)

# Grab every item from nums
my_list = [n for n in nums]
print(my_list)

# I want n*n for each item in nums
my_list = [n*n for n in nums]
print(my_list)

# I want n for each n in nums if n is even
my_list = [n for n in nums if n%2 == 0]
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in 0123
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' with numbers 0123 (a,0), (b,1)...
my_list = [(chr(97+num), num) for num in range(4)] #chr(65+num) for capital letters (A,B,C...)
#my_list = [(chr(945+num), num) for num in range(4)] #chr(65+num) for capital letters (A,B,C...)
print(my_list)


# Nested lists

alist = ["Hello", "What", 5]

mylist = [[x] for x in alist] # [['Hello'], ['What'], [5]]
print(mylist)

mylist = [alist*2 for x in range(2)] # [['Hello', 'What', 5, 'Hello', 'What', 5], ['Hello', 'What', 5, 'Hello', 'What', 5]]
print(mylist)

mylist = [[alist[x]*3] for x in range(alist.__len__())] # [['HelloHelloHello'], ['WhatWhatWhat'], [15]]
print(mylist)


# if/else

alist = [x for x in range(1, 21)]
print(alist)

mylist = [x*10 if x <= 10 else x*2 for x in alist]
print(mylist)