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

