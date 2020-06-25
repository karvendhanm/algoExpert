import timeit

mysetup = '''
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum_OofNSquared(array, targetSum):
    # Write your code here.

    l = len(array)
    for i in range(l - 1):
        _first = array[i]
        for j in range(i + 1, l):
            _second = array[j]
            if (_first + _second) == targetSum:
                return [_first, _second]
    return []
'''

mystmt = "twoNumberSum_OofNSquared(array, targetSum)"
timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)

