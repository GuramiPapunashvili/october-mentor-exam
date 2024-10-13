#Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. 
#There are no duplicates in the array.

def findmissing(arr):
    if len(arr) == 1:
        return arr[0] + 1
    n = len(arr) + 1
    for i in range(1,n):
        if i not in arr:
            return i
        
print(findmissing([4]))