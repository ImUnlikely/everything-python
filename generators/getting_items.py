from basic_square_numbers_generator import square_numbers

# Define numbers
nums = [1,2,3,4,5]

# Instantiating the generator
my_nums = square_numbers(nums) 

print(my_nums) # out:<generator object square_numbers at 0x000001A3C0103A20>

# 'next' gets the next result in a given iterator
print(next(my_nums)) # First item
print(next(my_nums)) # Second item
print(next(my_nums)) # Third item
print(next(my_nums)) # Fourth item
print(next(my_nums)) # Fifth item
try:
    print(next(my_nums)) # StopIteration error (only five items in list)
except Exception as identifier:
    print(f"Iterator exhausted, got {type(identifier)} error")

# Iterator is now exhausted, no results will be given by the below for loop

for num in my_nums:
    print(num)

    
my_nums = square_numbers(nums) # Instantiating the generator again

for num in my_nums:
    print(num)  # Now we get results
