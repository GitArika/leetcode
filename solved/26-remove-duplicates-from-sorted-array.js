/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  const list = new Set();

  for (let i = nums.length - 1; i >= 0; i--) {
    list.add(nums[i])
  }

  [...list.values()].forEach(el => nums.unshift(el))
  return [...list.values()].length;
};