import math

def is_prime(n):
    
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

is_prime(n=9)