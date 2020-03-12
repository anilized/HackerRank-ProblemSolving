import math
def getTotalX(a, b):
    # LCM (Least Common Multiple - CMMMC) of array a
    lista_LCM = []
    for LCM in range(max(a), min(b)+1):
        if all(LCM % nr == 0 for nr in a):
            lista_LCM.append(LCM)

    # GCM (Greatest Common Divisor - CMMDC) of array b
    if len(b) == 1:
        GCD = b[0]
    else:
        GCD = math.gcd(b[0], b[1])
        for i in range(len(b)):
            GCD = math.gcd(GCD, b[i])
        
    ###
    count = 0
    for i in range(len(lista_LCM)):
        if GCD % lista_LCM[i] == 0:
            count += 1
    return(count) 