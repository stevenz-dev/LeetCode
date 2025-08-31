# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

# Tortoise and Hare Algorithm
# https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode
# https://www.youtube.com/watch?v=zbozWoMgKW0
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # fast catches up with slow
                return True

        return False


def build_linked_list_with_cycle(lst, pos):
    if not lst:
        return None

    dummy = ListNode(0)
    cur = dummy
    cycle_entry = None

    for i, val in enumerate(lst):
        cur.next = ListNode(val)
        cur = cur.next
        if i == pos:
            cycle_entry = cur

    if pos != -1:
        cur.next = cycle_entry

    return dummy.next

head = build_linked_list_with_cycle([3,2,0,-4], 1)
print(Solution().hasCycle(head))  # True