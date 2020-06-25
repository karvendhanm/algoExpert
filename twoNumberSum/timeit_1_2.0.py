import timeit

mysetup = '''
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum_OofN(array, targetSum):
    # Write your code here.

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
'''

mystmt = "twoNumberSum_OofN(array, targetSum)"
timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)