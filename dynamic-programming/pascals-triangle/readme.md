#  Pascal's Triangle ✅
- **📁 Difficulty**  
  🟢 Easy  

## Description

Given an integer `numRows`, return the first `numRows` of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![pascals-triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
 

### Example 1:

> Input: numRows = 5

> Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

### Example 2:

> Input: numRows = 1

> Output: [[1]]
 

### Constraints:

- 1 <= numRows <= 30

## Topics
Dynamic Programming
Array

## Solution
- **Time complexity:** 
  - O(n²)
- **Space complexity:** 
  - O(n²)

```py
class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    ans = [[1]]

    if numRows == 1: return ans

    for i in range(numRows -1):
      n = len(ans[i])
      sub = [1]
      for k in range(n):
        if k + 1 < n:
          sub.append(ans[i][k] + ans[i][k+1])
      sub.append(1)
      ans.append(sub)
      
    return ans
```