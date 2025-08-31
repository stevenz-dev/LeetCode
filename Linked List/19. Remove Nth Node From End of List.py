import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

class Solution(object):
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/9032/Python-concise-one-pass-solution-with-dummy-head.
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Use a dummy node to avoid the special case of deleting the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast pointer (n+1) steps ahead
        # This ensures that when fast reaches the end,
        # slow will be right before the node to be deleted
        for i in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        # slow is the node before the node needs to be deleted
        slow.next = slow.next.next

        return dummy.next


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next

# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.

solution = Solution()

head = [1,2,3,4,5]
# head = [1]
n = 2
head = list_to_linked_list(head)

print(solution.removeNthFromEnd(head, n))
