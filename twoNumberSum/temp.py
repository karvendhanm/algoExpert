import timeit

def twoNumberSum(array, targetSum):
    _dict = {}
    for elem in array:
        desired_number = targetSum - elem

        if desired_number in _dict:
            return [elem, desired_number]
        else:
            _dict[elem] = True

    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

twoNumberSum(array, targetSum)

