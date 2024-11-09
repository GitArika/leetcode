# Invert Binary Tree ✅
- **📁 Difficulty**  
  🟢 Easy 

## Description
Given the `root` of a binary tree, invert the tree, and return its `root`.

### Example 1:
![example1](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

> Input: root = [4,2,7,1,3,6,9]

> Output: [4,7,2,9,6,3,1]

### Example 2:
![example2](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

> Input: root = [2,1,3]

> Output: [2,3,1]

### Example 3:

> Input: root = []

> Output: []

### Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Topics
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

## Solution 
- **Time complexity:**
    - O(n)
- **Space complexity:**
    - O(n)

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root

        temporary = root.left
        root.left = root.right
        root.right = temporary

        Solution.invertTree(self, root.left)
        Solution.invertTree(self, root.right)

        return root
```