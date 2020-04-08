# brute force

def angryProfessor(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    if count >= k:
        return "NO"
    else:
        return "YES"

a = [-1, 0, 1, 2]
k = 2

print(angryProfessor(k,a))