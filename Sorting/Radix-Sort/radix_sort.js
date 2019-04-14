module.exports = radixSort;


function radixSort(nums) {

    // make bins for digits.
    bins = [];
    for (var i = 0; i < 10; ++i) {
        bins.push([]);
    }

    // Find max number to get max number of digits
    var maxDigits = nums.reduce(function (a, b) {
        return Math.max(a,b);
    }).toString().length;

    var mod_value = 10;

    while (maxDigits > 0) {

        // bin in queues by current digit position.
        while (nums.length > 0) {
            var num = nums.shift();
            bins[Math.floor((num % mod_value) / (mod_value / 10))].push(num);
        }

        // unbin from queues back to array.
        for (var i = 0; i < 10; ++i) {
            while (bins[i].length > 0) {
                nums.push(bins[i].shift());
            }
        }

        mod_value *= 10;
        --maxDigits;
    }

    return nums;
}
