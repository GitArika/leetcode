function searchInsert(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;
  let mid: number
  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (nums[mid] > target) {
      if (left === right) {
        return mid;
      } else {
        right = mid - 1;
      }
    } else if (nums[mid] < target) {
      if (left === right) {
        return mid + 1
      } else {
        left = mid + 1;
      }
    } else if (nums[mid] === target) {
      return mid;
    }
  }
  return left
};