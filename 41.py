from itertools import permutations
import math

def is_prime(n):
    for i in range(2 ,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(9, 1, -1):
    for o in permutations(list(range(i, 0, -1))):
        n = int(''.join((str(z) for z in list(o))))
        if is_prime(n):
            print(n)
            break