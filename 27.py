import math
def is_prime(n):
    n = abs(n)
    for i in range(2 ,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


m = 0
ma = 0
mb = 0
r = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0 
        while is_prime(pow(n, 2) + a * n + b):
            n += 1
        print(n, a, b)
        if n > m:
            m = n
            ma = a
            mb = b
print(ma * mb)
            