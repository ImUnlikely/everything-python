# :=

alist = [1, 2, 3, 4]
if (n := len(alist)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# makes len(alist) a variable that can be used later
# reduces code duplication and improves readability

print(n) # is defined globally

#check if last item in range
for i in range(mx := len(alist)):
    if i == mx-1:
        print("Last iteration!")

# From: https://www.python.org/dev/peps/pep-0572/#syntax-and-semantics

# Handle a matched regex
if (match := pattern.search(data)) is not None:
    # Do something with match

# A loop that can't be trivially rewritten using 2-arg iter()
while chunk := file.read(8192):
   process(chunk)

# Reuse a value that's expensive to compute
[y := f(x), y**2, y**3]

# Share a subexpression between a comprehension filter clause and its output
filtered_data = [y for x in data if (y := f(x)) is not None]