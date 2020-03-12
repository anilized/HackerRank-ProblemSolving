def breakingRecords(scores):
    maxCount = 0
    minCount = 0
    indx = []
    minScore = scores[0]
    maxScore = scores[0]
    for i in range(len(scores)):
        if minScore < scores[i] and scores[i] > maxScore:
            maxCount += 1
            maxScore = scores[i]
        elif minScore > scores[i]:
            minCount += 1
            minScore = scores[i]
    indx.append(maxCount)
    indx.append(minCount)
    print(indx)


scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
scores2 = [100, 45, 41, 60, 17, 41, 45, 43, 100, 40, 89, 92, 34, 6, 64, 7, 37, 81, 32, 50]
breakingRecords(scores2)