def getMoneySpent(keyboards, drives, b):
    l = []
    drives.sort()
    keyboards.sort(reverse= True)
    for i in keyboards:
        for j in drives:
            if i + j > b:
                break
            else:
                l.append(i+j)
    if l:
        return max(l)
    else:
        return -1
    




keyboards = [40,50,60]
drives = [5,8,12]
b = 60

print(getMoneySpent(keyboards, drives, b))