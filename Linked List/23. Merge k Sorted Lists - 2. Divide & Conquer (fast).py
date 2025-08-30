from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

# Python3 - 2. Divide & Conquer (fast) 84.49%
# https://www.youtube.com/watch?v=q5a5OiGbT6Q&ab_channel=NeetCode
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i+1 == len(lists):
                    merged.append(lists[i])
                else:
                    merged.append(self.mergeTwoLists(lists[i], lists[i+1]))
            lists = merged

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        dummy = ListNode()
        cur = dummy

        # traverse two lists
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # attach the remaining nodes
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next


def build_linked_list(lst):
    dummy  = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

solution = Solution()

lists = []
lists.append(build_linked_list([1,4,5]))
lists.append(build_linked_list([1,3,4]))
lists.append(build_linked_list([2,6]))

print(solution.mergeKLists(lists))