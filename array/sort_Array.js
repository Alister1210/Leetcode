//Sort an array of 0’s 1’s 2’s without using extra space or sorting algo in-place
var sortColors = function (nums) {
  let a = 0,
    b = 0,
    c = nums.length - 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[a] == 0) {
      [nums[a], nums[b]] = [nums[b], nums[a]];
      a++;
      b++;
    } else if (nums[a] == 1) {
      a++;
    } else {
      [nums[a], nums[c]] = [nums[c], nums[a]];
      c--;
    }
  }
  return nums;
};

console.log(sortColors([2, 0, 2, 1, 1, 0]));
