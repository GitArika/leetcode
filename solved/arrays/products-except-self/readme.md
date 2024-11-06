# Product of Array Except Self ✅
- **📁 Difficulty**  
  🟡 Medium

## Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### Example 1:

> Input: nums = [1,2,3,4]

> Output: [24,12,8,6]

### Example 2:

> Input: nums = [-1,1,0,-3,3]

> Output: [0,0,9,0,0]
 
### Constraints:

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


## Topics
- Array
- Prefix Sum

## Solution
- **Space complexity:** O(n)
- **Time complexity:** O(1)

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate left products for each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and update the answer array
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
```