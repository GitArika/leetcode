# Shortest Subarray with Sum at Least K ❌
- **📁 Difficulty**  
  🔴 Hard

## Description

Given an integer array `nums` and an integer `k`, return the _length_ of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1.`

A subarray is a contiguous part of an array.

### Example 1:

> Input: nums = [1], k = 1

> Output: 1

### Example 2:

> Input: nums = [1,2], k = 4

> Output: -1

### Example 3:

> Input: nums = [2,-1,2], k = 3

> Output: 3
 
### Constraints:

- 1 <= nums.length <= 105
- -105 <= nums[i] <= 105
- 1 <= k <= 109


## Topics
- Array
- Binary Search
- Queue
- Sliding Window
- Heap (Priority Queue)
- Prefix Sum
- Monotonic Queue

## Solution
- **Time complexity:** 
  O(n log n)
- **Space complexity:** 
  O(1)

```py
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: 
          if nums[0] != k: return -1
          else: return 1

        ans, ac, a, p, c, sw = float('inf'), 0, 0, 0, 0, 0
        n = len(nums)
        
        while a < n:
            if nums[a] >= k: return 1
            
            ac = nums[a]
            c = 1
            p = a

            while ac < k:
                p+= 1
                c+= 1
                if p == n: break
                ac+= nums[p]
                if nums[p] < 0 and sw < a :
                    sw = p+1

            if ac >= k:
              if c < ans:
                ans = c

            if a + 1 == n:
               break
            elif nums[a] < nums[a + 1]:
               a += 1
               continue
            elif sw > a:
              a = sw
              continue
            a += 1

        return ans if ans != float('inf') else -1

# TODO: solve test case 79
nums = [17985,-36292,-23941,80618,20594,-6181,9181,65796,-25716,66593,-6873,34062,29878,852,-4767,-36415,11783,8085,-41063,-39940,74284,66272,82385,51634,-48550,9028,-30777,86509,44623,9413,-38369,-1822,46408,35217,72635,-16560,85373,52105,39477,3852,45974,-21593,15481,47280,73889,-42981,54978,95169,-19615,93133]
expect = 11

shortestSubarray = Solution.shortestSubarray(None, nums, 387303)
result = "Success" if shortestSubarray == expect else "Error"

print(f"8 - {result}! Expect: {expect} to Equal: {shortestSubarray}")        
```