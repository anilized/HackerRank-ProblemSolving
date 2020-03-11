# She can only blows the tallest ones

# [3, 2, 1, 3] -> Output 2

# This solution may not be the best because of O(n) on for loop


def birthdayCakeCandles(ar):
    count = 0
    a = sorted(ar)
    max_ar = a[-1]
    for i in ar:
        if i == max_ar:
            count += 1
    print(count)
    

birthdayCakeCandles([2,1,2,3,3,3])