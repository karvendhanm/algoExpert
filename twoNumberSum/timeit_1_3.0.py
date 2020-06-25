import timeit

mysetup = '''
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []    
'''

mystmt = "twoNumberSum(array, targetSum)"
timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)