def catAndMouse(x, y, z):
    if abs(z - y) == abs(z - x):
        return "Mouse C"
    else:
        if abs(z-y) > abs(z-x):
            return "Cat A"
        else:
            return "Cat B"

print(catAndMouse(1,2,3))