
def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s



s = 3
r = 0
while True:
    if sum(factorial(int(i)) for i in str(s)) == s:
        r += s
        print(r)
    s += 1
