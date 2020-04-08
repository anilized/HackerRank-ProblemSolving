def viralAdvertising(n):
    a = 5
    b = 2
    c = 2
    for _ in range(2, n+1):
        a = (a//2)*3
        b = a//2
        c += b
    return c

print(viralAdvertising(4))