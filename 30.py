s = 0
n = 11 
while True:
    if sum(pow(int(i), 5) for i in str(n)) == n:
        s += n
        print(n, s)
    n += 1
