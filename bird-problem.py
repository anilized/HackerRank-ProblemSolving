def migratoryBirds(arr):
    typecount = [0 for i in range(5)]
    for i in arr:
        typecount[i-1] += 1
        print(typecount)
    max_count = max(typecount)
    print(max_count)
    for i in range(5):
        if typecount[i] == max_count:
            return i+1
print(migratoryBirds([1, 4, 4, 4, 5, 3]))
