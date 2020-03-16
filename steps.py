# UDDDUDUU

def countingValleys(s):
    v = 0
    level = 0
    for i in range(len(s)):
        if s[i] == 'U': level += 1
        if s[i] == 'D': level -= 1
        if level == 0 and s[i] == 'U':
            v += 1
    print(v)
        
    


s = "DDUUDDUDUUUD"
countingValleys(s)