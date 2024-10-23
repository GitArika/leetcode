"""
    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
    s: The input string.
"""
class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    count = 0
    result = 0

    for char in s:
      if char == '(':
        count += 1
      else:
        count -= 1
        if count < 0:
            result += 1
            count = 0

    result += count

    return result