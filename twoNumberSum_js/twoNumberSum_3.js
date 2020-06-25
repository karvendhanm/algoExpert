function twoNumberSum(array, targetSum) {


    let left = 0;
    let right = array.length - 1;

    while (left < right) {
        let currentSum = array[left] + array[right];
        if (currentSum === targetSum) {
            return [array[left], array[right]]
        } else if (currentSum < targetSum) {
            left++;
        } else if (currentSum > targetSum) {
            right--;
        }
    }

    return []
}



array = [3, 5, -4, 8, 11, 1, -1, 6];
targetSum = 10;

console.log(twoNumberSum(array, targetSum))