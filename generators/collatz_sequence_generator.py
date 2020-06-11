def collatz_sequence_generator(n):
    """generates a collatz sequence where n = term1

    Args:
        n (int): any positive real number

    Yields:
        int: the next term of the sequence
    """
    yield n # n = n = 1st term
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            yield n
        else:
            n = int((n*3) + 1)
            yield n



# Related generator (used in project euler)
def collatz_sequence_length_generator(start, stop):
    """generates the length of collatz sequences where start <= n <= stop

    Args:
        start (int): the first number to check
        stop (int): the last number to check (inclusive)

    Yields:
        int, int: n and the length of n's sequence
    """
    
    for x in range(start, stop+1):
        cgen = collatz_sequence_generator(x)
        count = 0
        for term in cgen:
            count += 1

        yield x, count

mygen = collatz_sequence_length_generator(1, 1000000)

longest = 0
biggest = 0
for num, length in mygen:
    if length > longest:
        print(f"n={num} chain is {length} terms")
        longest = length
        biggest = num

print(f"The number with the longest chain is {biggest} with a chain of {longest} terms")