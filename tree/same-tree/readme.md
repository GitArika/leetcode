# Same Tree ✅
- **📁 Difficulty**  
  🟢 Easy 

## Description
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Example 1:

![example1](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

> Input: p = [1,2,3], q = [1,2,3]

> Output: true


### Example 2:
![example2](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

> Input: p = [1,2], q = [1,null,2]

> Output: false

### Example 3:
![example3](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

> Input: p = [1,2,1], q = [1,1,2]

> Output: false
 

### Constraints:

- The number of nodes in both trees is in the range [0, 100].
- -104 <= Node.val <= 104

## Topics
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

## Solution
- **Time complexity:**
    - O(log n) in the best case for a balanced tree
    - O(n) in the worst case where n is the total nodes in both threes
- **Space complexity:**
    - O(log n) in the best case for a balanced tree
    - O(n) in the worst case for an unbalanced tree.

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        
        # -10ˆ4 <= Node.val <= 10ˆ4 
        if p.val > 0:
            right = Solution.isSameTree(self, p.right, q.right)
            if right is False:
                return False
            
            left = Solution.isSameTree(self, p.left, q.left)
            if left is False:
                return False
        else: 
            left = Solution.isSameTree(self, p.left, q.left)
            if left is False:
                return False
                                    
            right = Solution.isSameTree(self, p.right, q.right)
            if right is False:
                return False
            
        return True
```