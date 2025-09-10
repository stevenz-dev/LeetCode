from typing import Optional

"""
题目

给你一个链表的头节点 head, 将链表向右旋转 k 个位置。

例子：

输入: head = 1 → 2 → 3 → 4 → 5, k = 2
输出: 4 → 5 → 1 → 2 → 3



🔑 思路

处理特殊情况
    如果链表为空、只有一个节点, 或者 k=0, 直接返回 head。

先计算链表长度 n
    因为 k 可能大于 n, 所以真正要旋转的次数是 k % n。
    如果 k % n == 0, 说明旋转一圈后不变, 直接返回 head。

形成环
    把链表尾部接到头部, 形成一个环。

找到新的断点
    新的头节点是 (n - k % n) 位置的下一个节点。
    遍历到 (n - k % n) 节点, 让它的 next 断开即可。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. compute length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. mod k
        k = k % length
        if k == 0:
            return head

        # 3. make it circular
        tail.next = head

        # 4. find new head (length - k steps from start)
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head