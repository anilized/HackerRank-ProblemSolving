def utopianTree(n):
    h = 1
    for i in range(1,n+1):
        if n == 0:
            return 1
        else:
            if (i % 2 == 0):
                h += 1
            elif (i % 2 == 1):
                h = 2 * h
    return h

n = 1

print(utopianTree(0))