
def jumpingOnClouds(c):
    if 2 < len(c) and c[2] != 1:
        return 1 + jumpingOnClouds(c[2:])
    if 1 < len(c) and c[1] != 1:
        return 1 + jumpingOnClouds(c[1:])
    else:
        return 0

        

c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))