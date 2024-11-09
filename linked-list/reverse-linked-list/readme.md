# Reverse Linked List ✅
- **📁 Difficulty**  
  🟢 Easy  

## Description

Given the `head` of a singly linked list, reverse the list, and return the _reversed list_. 

### Example 1:
![example1](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

> Input: head = [1,2,3,4,5]
> Output: [5,4,3,2,1]


### Example 2:
![example2](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

> Input: head = [1,2]

> Output: [2,1]

### Example 3:

> Input: head = []

> Output: []
 

### Constraints:

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

## Topics
- Linked List

## Solution
- **Time Complexity:**: 
  - O(n)
- **Space Complexity:**: 
  - O(1)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
```
