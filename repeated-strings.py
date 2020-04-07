# return the count
# count s[:mod]



def repeatedString(s, n):
    length = len(s)
    mod = n % length
    times = n // length
    count = s.count('a')
    return (count * times) + s[:mod].count('a') 
    


s = "aba"
n = 10

print(repeatedString(s,n))
