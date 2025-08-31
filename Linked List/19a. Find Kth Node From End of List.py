from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

class Solution:
    def findKthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # move fast k steps ahead
        for _ in range(k):
            fast = fast.next

        # move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        return slow

def build_linked_list(lst):
    dummy  = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

"""
Problem Statement
------------------
Given the head of a singly linked list and an integer k, return the k-th node from the end of the list.

If k is greater than the length of the list, return None.

Example 1
Input:  head = 1 → 2 → 3 → 4 → 5,  k = 2
Output: Node with value 4
Explanation: The 2nd node from the end is node 4.

Example 2
Input:  head = 1 → 2 → 3,  k = 3
Output: Node with value 1
"""
head = [1, 2, 3, 4, 5]
k = 2
print(Solution().findKthFromEnd(build_linked_list(head), k))
