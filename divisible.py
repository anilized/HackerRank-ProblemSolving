def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

# Not an OK solution because it runs on O(n^2) time1