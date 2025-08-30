import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

    # LeetCode does not support this
    # def __lt__(self, other):
    #     return self.val < other.val

# Python3 - 3. heapq - tuple
class Solution:
    # https://www.youtube.com/watch?v=ptYUCjfNhJY
    # https://www.youtube.com/watch?v=kpCesr9VXDA
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to always extract the smallest node
        heap = []
        for i, node in enumerate(lists):
            if node:
                # Push (value, index, node) to avoid comparison error when values are equal
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                # Push the next node of the current list into the heap
                heapq.heappush(heap, (node.next.val, i, node.next))

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
