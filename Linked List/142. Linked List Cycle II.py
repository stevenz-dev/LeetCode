from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{} → {}".format(self.val, self.next)
'''
乌龟和兔子算法, 也就是Floyd环检测算法, 的基本思路是设置两个指针, 一个快一个慢, 在遍历链表的过程中, 如果存在环, 那么快指针（兔子）和慢指针（乌龟）会在环内的某个位置相遇。

如果有环, 设环的长度为C, 从链表头到环的起始节点的距离为A, 从环的起始节点到乌龟和兔子首次在环内相遇的节点的距离为B。

当乌龟和兔子首次在环内相遇时, 乌龟走过的总路程为 A+B, 兔子走过的总路程为 A+nC+B, 其中n为兔子在环内多转的圈数。因为兔子的速度是乌龟的两倍, 所以兔子走过的总路程是乌龟的两倍, 即 2*(A+B) = A+nC+B。化简后得到 A = (n-1)C + (C-B)。

等式右边 (n-1)C + (C-B) 的含义是：从环的起始节点开始, 兔子再走(n-1)圈, 然后再走(C-B)的距离, 正好可以再次走到乌龟和兔子首次相遇的节点。

所以, 当乌龟和兔子首次相遇后, 如果此时让兔子回到链表头部, 且速度和乌龟一样, 那么兔子和乌龟将会在环的起始节点再次相遇。
'''
# Floyd’s Tortoise and Hare Algorithm
# https://www.youtube.com/watch?v=LUm2ABqAs1w
class Solution(object):
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # step 1: check if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # cycle detected
                break
        else:
            return None        # no cycle

        # step 2: find cycle entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
