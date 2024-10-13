#Given an array of integers, find all unique pairs of elements that sum to a given target number.

def findPairs(arr,target):
    pairs = {

    }
    for i in arr:
        for x in arr:
            if i + x == target:
                 pairs.update({i:x})
    output_until = len(pairs) // 2
    to_return = list(pairs.items())[:output_until]
    return to_return

print(findPairs([-1, 0, 1, 2, -2, 3], 0))