def combination_gen():
    """generates combinations where x, y, z are between 1 and 1000

    Yields:
        int, int, int: 
    """
    for x in range(1, 1001):
        for y in range(1, 1001):
            for z in range(1, 1001):
                yield x, y, z

# Example usage:
# Find pythegorean triplet
mygen = combination_gen()
for a, b, c in mygen:
    if (a + b + c == 1000) and (a < b < c):
        if (a**2 + b**2 == c**2):
            print(f"a={a}\nb={b}\nc={c}\nProduct={a*b*c}")
            break