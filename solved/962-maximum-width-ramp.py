class Solution:
  def maxWidthRamp(self, nums: List[int]) -> int:
    stack = []
    n = len(nums)
    maxWidth = 0

    for i in range(n):
      if not stack or nums[stack[-1]] >= nums[i]:
        stack.append(i)

    for i in range(n - 1, -1, -1):
      while stack and nums[stack[-1]] <= nums[i]:
        j = stack.pop()
        maxWidth = max(maxWidth, i - j)

    return maxWidth