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