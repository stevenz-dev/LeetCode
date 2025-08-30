from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p = head
        head1 = p1 = ListNode()
        head2 = p2 = ListNode()

        count_p1 = 0
        count_p2 = 0
        while p:
            print(' head:', head)
            print('    p:', p)
            print()
            print('head1:', head1)
            print('       ' + '    ' * count_p1 + '↑')
            print('       ' + '    ' * count_p1 + 'p₁')
            print()
            print('head2:', head2)
            print('       ' + '    ' * count_p2 + '↑')
            print('       ' + '    ' * count_p2 + 'p₂')
            if p.val < x:
                p1.next = p
                p1 = p1.next
                count_p1 += 1
            else:
                p2.next = p
                p2 = p2.next
                count_p2 += 1
            p = p.next
            print('-'*35)
            print(' head:', head)
            print('    p:', p)
            print()
            print('head1:', head1)
            print('       ' + '    ' * count_p1 + '↑')
            print('       ' + '    ' * count_p1 + 'p₁')
            print()
            print('head2:', head2)
            print('       ' + '    ' * count_p2 + '↑')
            print('       ' + '    ' * count_p2 + 'p₂')
            print('-'*35)

        # This is important!
        # point p2.next to none, in case p2.next has more nodes
        p2.next = None
        # connect p1.next to head2.next
        p1.next = head2.next

        return head1.next

def build_linked_list(lst):
    dummy  = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy .next

'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''
head = [1, 4, 3, 2, 5, 2]
x = 3
print(Solution().partition(build_linked_list(head), x))
