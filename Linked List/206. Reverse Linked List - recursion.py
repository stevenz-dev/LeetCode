# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        # print('new_head:', new_head)
        # print('head:', head)
        head.next.next = head
        head.next = None
        # print('new_head:', new_head)
        # print('head:', head)
        # print()
        return new_head


def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next


head = list_to_linked_list([2,6,7,0,5,3])

# test case
solution = Solution()

cur = head

while cur:
    if cur.next:
        print(cur.val, '->', end=" ")
    else:
        print(cur.val, '->', cur.next)
    cur = cur.next

newList = solution.reverseList(head)

while newList:
    if newList.next:
        print(newList.val, '->', end=" ")
    else:
        print(newList.val, '->', newList.next)
    newList = newList.next