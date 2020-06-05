# the + sign

# add numbers
x = 1
y = 5

z = x + y # 6
print(z)

z = x + 5 # 6
print(z)

z = + 5 # 5
print(z)

z = (x * 5) + 5 # 10
print(z)


# strings
str1 = "Hello!"
str2 = "What?"

mystring = str1 + str2
print(mystring)

mystring = str1 + " " + str2
print(mystring)

try:
    mystring = str1 + " " + str2 + 5
    print(mystring)
except TypeError as error:
    print(f"Can only concatenate str to str (not int) {type(error)}")
finally:
    mystring = str1 + " " + str2 + " 5" + " It's a number, but as a string"
    print(mystring)

mystring = str1 + " " + str(x+y) # 5+1 = 6
print(mystring)
