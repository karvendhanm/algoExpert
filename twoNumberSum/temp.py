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

def twoNumberSum_(array, targetSum):
    # Write your code here.
    nums = {}
    for idx, num in enumerate(array):
        required_num = targetSum - num
        pop_num = array.pop(idx)
        if required_num in array:
            return [num, required_num]
        array.insert(pop_num, idx)
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

twoNumberSum(array, targetSum)
twoNumberSum_(array, targetSum)

