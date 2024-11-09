# Merge Two Sorted Lists ✅
- **📁 Difficulty**  
  🟢 Easy  

## Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
![example1](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

> Input: list1 = [1,2,4], list2 = [1,3,4]

> Output: [1,1,2,3,4,4]

### Example 2:

> Input: list1 = [], list2 = []

> Output: []


### Example 3:

> Input: list1 = [], list2 = [0]

> Output: [0]
 

### Constraints:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Topics
- Linked List
- Recursion

## Solution
- **Time Complexity:**: 
  - O(n+m)
- **Space Complexity:**: 
  - O(1)

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  if (list1 === null) return list2
  if (list2 === null) return list1

  const merge = new ListNode(undefined);
  let pointer1 = list1, pointer2 = list2, pointerMerge = merge

  while (pointer1 !== null || pointer2 !== null) {
    if (pointer1 === null) {
      pointerMerge.val = pointer2.val
      pointer2 = pointer2?.next
    } else if (pointer2 === null) {
      pointerMerge.val = pointer1.val
      pointer1 = pointer1?.next
    } else if (pointer1.val <= pointer2.val) {
      pointerMerge.val = pointer1.val
      pointer1 = pointer1?.next
    } else {
      pointerMerge.val = pointer2.val
      pointer2 = pointer2?.next
    }

    pointerMerge.next = pointer1 !== null || pointer2 !== null ? new ListNode() : null
    pointerMerge = pointerMerge.next
  }

  return merge;
};
```