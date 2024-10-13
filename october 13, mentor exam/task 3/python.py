# Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times.
# You may assume that the array is non-empty and the majority element always exists in the array.

def findMajority(arr):
    n = len(arr)
    for i in arr:
        if arr.count(i) > n // 2:
            return i
        
print(findMajority(0))