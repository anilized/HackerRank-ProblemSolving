def pageCount(n,p):
    total = n//2
    right = p//2
    left = total - right
    if (right > left):
        return int(left)
    else:
        return int(right)

print(pageCount(6,5))