def sockMerchant(n, ar):
    counter_set = set()
    count = 0
    for i in range(len(ar)):
        element = ar[i]
        if (element in counter_set):
            counter_set.remove(element)
            count += 1
        else:
            counter_set.add(element)
    return count

n = 9

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9,ar))