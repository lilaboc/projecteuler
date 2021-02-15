import math
def factors(n):
    count = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            count += 1
    return count * 2



n = 0
t = 0
while True:
    n += 1
    t += n
    f = factors(t)
    print(t, f)
    if f >= 500:
        print(t)
        break
