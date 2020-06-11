from math import sqrt

def prime_generator():
    """generates prime numbers
    """

    def is_prime(n):
        """checks if n is prime

        Args:
            n (int): any real number

        Returns:
            bool: True if n is prime, False if n is not prime
        """
        i = 3
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i = i + 2

        return True

    yield 2 # the first prime
    n = 1

    while True:
        n += 2
        if is_prime(n):
            yield n

mygen = prime_generator()

print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))