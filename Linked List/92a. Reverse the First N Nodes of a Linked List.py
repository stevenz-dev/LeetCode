# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)


class Solution(object):
    # 用于记录第 n+1 个节点
    successor = None

    def reverseN(self, head, n):
        global successor
        if n == 1:
            # 记录第 n+1 个节点
            successor = head.next
            return head

        # 反转以 head.next 为起点的 n-1 个节点
        new_head = self.reverseN(head.next, n-1)

        head.next.next = head
        # 连接反转后的链表和后面的链表
        head.next = successor
        return new_head


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([2, 6, 7, 0, 5, 3])
print(head)
print(Solution().reverseN(head, 3))
