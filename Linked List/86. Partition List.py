from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()   # list for < x
        large = ListNode()   # list for >= x
        p1 = small
        p2 = large

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        # This is important!
        # point p2.next to none, in case p2.next has more nodes (prevent cycle)
        p2.next = None
        # connect p1.next to large.next
        p1.next = large.next

        return small.next

def build_linked_list(lst):
    dummy  = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''
head = [1, 4, 3, 2, 5, 2]
x = 3

head = build_linked_list(head)

print("head:")
print(head)

print("After partitioning around", x, ":")
print(Solution().partition(head, x))
