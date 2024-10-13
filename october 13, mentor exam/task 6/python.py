#Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.

def meanOfArrs(arr1,arr2):
    joined = arr1 + arr2
    return sum(joined) / len(joined)

print(meanOfArrs([1,2],[2,3]))