import math
def factors(n):
    yield 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if int(n / i) != i:
                yield int(n / i)


r = []
for i in range(1, 28124):
    if sum(factors(i)) > i:
        r.append(i)


s = set()
for i in r:
    for o in r:
        s.add(i + o)

print(sum(i for i in range(1, 28124) if i not in s))
