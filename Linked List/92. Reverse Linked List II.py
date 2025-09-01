from typing import Optional

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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        
        # 将反转的起点推进到第 left 个位置
        # 在递归的每一步中，我们将头节点向前推进一步，然后递减 left 和 right。这是为了找到需要反转的部分链表的起点，并且在递归的每一步中，都能准确地表示需要反转的链表部分的长度。
        # In each step of the recursion, we advance the head node one step forward and decrement both left and right. 
        # This is to locate the starting point of the section of the linked list that needs to be reversed, 
        # and to accurately represent the length of the part of the linked list to be reversed in each step of the recursion.
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

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


head = list_to_linked_list([1,2,3,4,5])
left = 2
right = 4
print(head)
print(Solution().reverseBetween(head, left, right))
