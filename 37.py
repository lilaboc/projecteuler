import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2 ,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


cache = set()
i = 11
count = 0
s = 0
while True:
    if is_prime(i):
        cache.add(i)
        for o in range(1, len(str(i))):
            if not is_prime(int(str(i)[:o])) or not is_prime(int(str(i)[-o:])):
                break
        else:
            s += i
            count += 1
            if count == 11:
                break
    i += 2
print(s)