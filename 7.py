import math
def is_prime(n):
    for i in range(2 ,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = 2
count = 0
while True:
    if is_prime(n):
        count += 1
        if count == 10001:
            print(n)
            break
    n += 1
