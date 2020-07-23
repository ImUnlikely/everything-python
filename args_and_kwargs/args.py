def myFunc(x, y, *args): # when using the '*' sign the variable becomes an iterable
    print(x+y)
    print(type(args)) # if Args is none then it is just an empty tuple
    for arg in args:
        print(arg)

myFunc(5, 4) # *args can be left empty
myFunc(5, 4, 6, "a string", [0, 1, ["nested lists", {"with":"dictionaries"}]], "cool")

def anotherFunc(a, b, *nums:int): # iterative args need to come last
    print(a, b)
    print(nums)
    print(sum(nums))

anotherFunc("This is", "a test", 3, 6, 5, 4, 100) # can pass as many arguments as we want