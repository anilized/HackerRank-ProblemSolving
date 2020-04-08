def saveThePrisoner(n, m, s):
    m %= n
    res = (m + s - 1) % n
    if res == 0:
        res = n
    print (res)

n = 5
m = 18
s = 2

saveThePrisoner(n,m,s)