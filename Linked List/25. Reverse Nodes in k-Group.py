# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 区间 [a, b) 包含 k 个待反转元素
        a, b = head, head
        for _ in range(k):
            # 不足 k 个，不需要反转，base case
            if not b:
                return head
            b = b.next

        # 反转前 K 个节点
        new_head = self.reverse(a, b)
        # 递归地反转剩下的节点，并链接到前 K 个节点后
        print(a, new_head)
        a.next = self.reverseKGroup(b, k)

        return new_head

    # 反转区间 [a, b) 的元素，左闭右开
    def reverse(self, a, b):
        # 3 pointers:
        # -------------------------------------
        #        cur
        #         ↓
        #  None   2 → 6 → 7 → 0 → 5 → 3 → None
        #   ↑         ↑
        #  pre       nxt

        pre, cur  = None, a

        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # 返回反转后的头结点
        return pre


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([1, 2, 3, 4, 5])
k = 2

# test case
solution = Solution()

print(head)
print(solution.reverseKGroup(head, k))
