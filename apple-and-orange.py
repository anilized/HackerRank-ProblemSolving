def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = addLoc(a,apples)
    oranges = addLoc(b,oranges)
    apple_count = 0
    orange_count = 0
    for i in apples:
        if i >= s and i <= t:
            apple_count += 1
    for i in oranges:
        if i >= s and i <= t:
            orange_count += 1
    return apple_count, orange_count

def addLoc(num,arr):
    for i in range(len(arr)):
        arr[i] += num
    return arr


s = 7
t = 10
a = 4
b = 12
apples = [2,3,-4]
oranges = [3,-2,-4]

print(addLoc(a,apples))
print(countApplesAndOranges(s,t,a,b,apples,oranges))