import math
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factors(n):
    return ((i for i in range(2, int(math.sqrt(n)) + 1) if n % i == 0))
            
for i in factors(600851475143):
    if is_prime(i):
        print(i)