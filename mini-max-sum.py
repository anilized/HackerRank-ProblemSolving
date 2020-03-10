"""
Given five positive integers, 
find the minimum and maximum values 
that can be calculated by summing exactly 
four of the five integers. 
Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.

a = [1,2,3,4,5]
min -> [1,2,3,4] = 10 -> [1:]
max -> [2,3,4,5] = 14

"""

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    mini = sum(sorted_arr[:-1])
    maxi = sum(sorted_arr[1:])
    print(mini, maxi)    

a = [1,2,3,4,5]
print(a[:-1])
print(a[1:])

b = [3,1,2,5]
c = sorted(b)
print(c)
print(miniMaxSum(a))