# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 3 pointers:
        # ------------------------------------
        #        head
        #         ↓
        # None    2 → 6 → 7 → 0 → 5 → 3 → None
        # ↑           ↑
        # p₁          p₂

        p1, p2 = None, head

        while head:
            p2 = head.next
            # 逐个结点反转
            head.next = p1
            # 更新指针位置
            p1 = head
            head = p2

        # 返回反转后的头结点
        return p1


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([2, 6, 7, 0, 5, 3])

# test case
solution = Solution()

print(head)
print(solution.reverseList(head))
