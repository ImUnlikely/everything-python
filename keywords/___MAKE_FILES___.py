import os

mypath = r"C:\Users\Thoma\Desktop\Code\Repositories\everything-python\keywords"

os.chdir(mypath)
print(os.getcwd())

for root, dir, file in os.walk(mypath):
    for filename in file:
        print(filename)


#open("sample.txt", "x")

filenames = [
    "True",
    "False",
    "None",
    "if",
    "elif",
    "else",
    "pass",
    "continue",
    "break",
    "lambda",
    "def",
    "return",
    "yield",
    "await",
    "import",
    "try",
    "except",
    "raise",
    "class",
    "finally",
    "is",
    "in",
    "not",
    "or",
    "and",
    "for",
    "as",
    "from",
    "nonlocal",
    "while",
    "assert",
    "del",
    "global",
    "with",
    "async"
]

for name in filenames:
    fname = name + ".py"
    open(fname, "x")

for root, dir, file in os.walk(mypath):
    for filename in file:
        print(filename)