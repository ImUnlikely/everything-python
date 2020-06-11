def fib_seq(term1=int(1), term2=int(2), highest=int(10)):
    """yields the next nunmber in the fibonacci sequence

    Args:
        term1 (int, optional): the first term of the sequence. Defaults to int(1).
        term2 (int, optional): the second term of the sequence. Defaults to int(2).
        highest (int, optional): the highest value in the sequence. Defaults to int(10).
    """

    x = term1
    y = term2

    if x == term1:
        yield x

    if y == term2:
        yield y

    while True:
        z = x + y
        x = y
        y = z

        if z <= highest:
            yield z
        elif z > highest:
            break
        else:
            pass

fib_gen = fib_seq(highest=100)

for x in fib_gen:
    print(x)