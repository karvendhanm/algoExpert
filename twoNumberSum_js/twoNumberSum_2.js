function twoNumberSum(array, targetSum) {

    const len = array.length;
    for (let i = 0; i < (len - 1); i++) {
        num_1 = array[i];
        for (let j = i + 1; j < len; j++) {
            num_2 = array[j];
            if ((num_1 + num_2) === targetSum) {
                return [num_1, num_2];
            }
        }
    }
    return [];
}

array = [3, 5, -4, 8, 11, 1, -1, 6];
targetSum = 10;

console.log(twoNumberSum(array, targetSum))