import timeit

mysetup = '''
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum_OofNSquared(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
    return []
'''

mystmt = "twoNumberSum_OofNSquared(array, targetSum)"
timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)