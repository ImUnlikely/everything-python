from math import sqrt 
  
def primeFactors(n):
    """generates the prime factors of n

    Args:
        n (int): any positive real number

    Yields:
        int: the i'th prime factor
    """
      
    while n % 2 == 0: 
        yield 2 
        n = n / 2
          
    for i in range(3,int(sqrt(n))+1,2): 
          
        while n % i == 0: 
            yield i 
            n = n / i 
              
    if n > 2: 
        yield n 
          
  
n = 600851475143
# n = 1001
gen = primeFactors(n)

for x in gen:
    print(x)