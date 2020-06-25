function twoNumberSum(array, targetSum) {

    const len = array.length;
    nums = {};
    for (let i = 0; i <= len; i++) {
        let num = array[i];
        let desired_number = targetSum - array[i];

        _bool = nums[desired_number];
        if (!_bool) {
            nums[num] = true;
        } else {
            return [desired_number, num];
        }
    }
    return [];
}


array = [3, 5, -4, 8, 11, 1, -1, 6];
targetSum = 10;

console.log(twoNumberSum(array, targetSum));
