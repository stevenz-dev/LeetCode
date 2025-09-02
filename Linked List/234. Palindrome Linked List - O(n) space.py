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
        left = head

        def traverse(head):
            nonlocal left
            if head is None:
                return True
            res = traverse(head.next)
            res = res and (head.val == left.val)
            left = left.next
            return res

        return traverse(head)


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([1, 2, 2, 1])
head = list_to_linked_list([1, 2])
print(head)

print(Solution().isPalindrome(head))
