#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    b=[]
    for i in range(len(a)-1):
        l=[]
        for j in range(i+1,len(a)):
            if a[j]-a[i]<=1:
                l.append(j)
            else:
                break
        b.append(len(l)+1)
        print(b)
    return max(b)

a = [4,6,5,3,3,1]
print(pickingNumbers(a))
