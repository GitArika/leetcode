# Minimum Size Subarray Sum
✅ Solved
Difficult: Medium

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, **return 0** instead.

## Example 1:

Input: 
target = 7 
nums = [2,3,1,2,4,3]
Output: 2

`Explanation: The subarray [4,3] has the minimal length under the problem constraint.`

Example 2:

Input: target = 4
nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11
nums = [1,1,1,1,1,1,1,1]
Output: 0 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

```py
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = math.inf 
        windowSum = 0
        windowStart = 0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= target:
                minLength = min(windowEnd - windowStart + 1, minLength)
                windowSum -= nums[windowStart]
                windowStart += 1
        return 0 if  minLength == math.inf else minLength
```
