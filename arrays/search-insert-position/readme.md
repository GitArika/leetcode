# Search Insert Position ✅
- **📁 Difficulty**  
  🟢 Easy 

## Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:

> Input: nums = [1,3,5,6], target = 5

> Output: 2

### Example 2:

> Input: nums = [1,3,5,6], target = 2

> Output: 1


### Example 3:

> Input: nums = [1,3,5,6], target = 7

> Output: 4
 

### Constraints:

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Topics
- Array
- Binary Search

## Solution

- **Time complexity:** O(log n)
- **Space complexity:** O(1)

```ts
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
```