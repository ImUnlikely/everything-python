def square_numbers(nums):
    """square number generator

    Arguments:
        nums {list/set} -- iterative, contains 1 or more numbers

    Yields:
        int -- square root of each number in nums
    """

    for i in nums:
        yield (i * i) # Does not store all results in memory
                      # Good for performance