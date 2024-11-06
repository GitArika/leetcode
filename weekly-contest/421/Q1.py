import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] * nums[0]
    
        initial_gcd = math.gcd(*nums)
        initial_lcm = math.lcm(*nums)
        initial_score = initial_gcd * initial_lcm
    
        max_score = initial_score
        for i in range(n):
            gcd_without_i = math.gcd(*nums[:i] + nums[i+1:])
            lcm_without_i = math.lcm(*nums[:i] + nums[i+1:])
            score_without_i = gcd_without_i * lcm_without_i
            max_score = max(max_score, score_without_i)
    
        return max_score