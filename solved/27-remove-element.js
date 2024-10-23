/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {

  const subArray = nums.filter(el => el !== val);
  subArray.forEach(el => {
    nums.unshift(el)
  });

  return subArray.length;
};