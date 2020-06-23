import numpy as np

def twoNumberSum_3(array, targetSum):
    _dict = {}
    for elem in array:
        desired_number = targetSum - elem
        if desired_number in _dict:
            return [desired_number, elem]
        else:
            _dict[elem] = True

    return []

def twoNumberSum_2(array, targetSum):
    for elem in array:

        desired_number = targetSum - elem
        if desired_number == elem:
            continue

        try:
            array.index(desired_number)
            return [elem, desired_number]
        except:
            continue
    return []

def twoNumberSum_1(array, targetSum):
    # Write your code here.

    l = len(array)
    for i in range(l - 1):
        _first = array[i]
        for j in range(i + 1, l):
            _second = array[j]
            if (_first + _second) == targetSum:
                return [_first, _second]
    return []


for idx in range(200):
    array =list(np.random.choice(range(-100, 100), size=np.random.choice(range(2, 20)), replace=False))
    targetSum = np.random.choice(range(-100, 100))
    print(array)
    print(targetSum)
    print(twoNumberSum_2(array, targetSum))
    print(twoNumberSum_3(array, targetSum))
    assert twoNumberSum_2(array, targetSum) == twoNumberSum_3(array, targetSum), 'two sum implementation is wrong'




