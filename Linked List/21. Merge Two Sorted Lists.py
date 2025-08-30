from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        dummy = ListNode()
        cur = dummy

        # traverse two lists
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # attach the remaining nodes
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next

# 1 -> 2 -> 4 -> None
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# 1 -> 3 -> 4 -> None
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))

print(list1)
print(list2)
print(Solution().mergeTwoLists(list1, list2))
