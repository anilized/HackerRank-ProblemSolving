def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reversed_day = int("".join(reversed(str(day))))
        if abs(reversed_day - day) % k == 0:
            count += 1
    return count