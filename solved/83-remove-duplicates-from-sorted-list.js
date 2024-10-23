
var deleteDuplicates = function (head) {
  if (!head || head.next === null) return head;

  let slow = head, fast = head;

  while (fast != null) {
    if (fast.val != slow.val) {
      slow.next = fast;
      slow = slow.next;
    }
    fast = fast.next;
  }
  slow.next = null;
  return head;
};