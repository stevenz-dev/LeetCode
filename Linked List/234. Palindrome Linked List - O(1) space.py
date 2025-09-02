from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. find middle (slow will stop at middle)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse second half
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # print(head, prev)

        # 3. compare two halves
        left, right = head, prev
        while right:  # right part is shorter or equal
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([1, 2, 2, 1])
print(head)
print(Solution().isPalindrome(head))
print()
head = list_to_linked_list([1, 2, 3, 2, 1])
print(head)
print(Solution().isPalindrome(head))
