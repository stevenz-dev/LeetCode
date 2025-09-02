from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.val, self.next)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast:
            if fast.val != slow.val:
                slow.next = fast   # link non-duplicate node
                slow = slow.next   # move slow
            fast = fast.next       # always move fast

        slow.next = None  # cut off any leftover duplicates
        return head