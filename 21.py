import math
def factors(n):
    yield 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            yield int(n / i)

n = 10000

r = 0
for i in range(2, n):
    # print(sum(factors(i)))
    b = sum(factors(i))
    if i == b:
        continue
    if i == sum(factors(b)):
        r += i

print(r)
# print(list(factors(220)))