import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} → {}".format(self.val, self.next)

class Solution(object):
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/9032/Python-concise-one-pass-solution-with-dummy-head.
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = ListNode()
        tmp.next = head
        head = tmp
        print()
        print('head:', head)

        p1 = p2 = head
        count_p1 = 0
        count_p2 = 0

        print('      ' + '↑')
        print('      ' + 'p₁')
        print()

        while count_p1 <= n:
            p1 = p1.next
            time.sleep(1)
            print('\033[3A', end='')
            if count_p1 == 0:
                print('      ↑   ' + '↑')
                print('      p₂  ' + 'p₁')
            else:
                print('      ↑   ' + '    ' * count_p1 + '↑')
                print('      p₂  ' + '    ' * count_p1 + 'p₁')
            print()
            count_p1 +=1
        
        while p1:
            p1 = p1.next
            p2 = p2.next
            time.sleep(1)
            print('\033[3A', end='')
            if count_p2 == 0:
                print('          ↑   ' + '    ' * (count_p1-1) + '↑')
                print('          p₂  ' + '    ' * (count_p1-1) + 'p₁')
            else:
                print('    ' * count_p2 + '          ↑   ' + '    ' * (count_p1-1-count_p2) + '↑')
                print('    ' * count_p2 + '          p₂  ' + '    ' * (count_p1-1-count_p2) + 'p₁')
            print()
            count_p1 +=1
            count_p2 +=1

        p2.next = p2.next.next
        print('head:', head)
        return head.next

def list_to_linked_list(lst):
    head = ListNode()
    current = head

    for val in lst:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next

    return head.next

# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.

solution = Solution()

head = [1,2,3,4,5]
# head = [1]
n = 2
head = list_to_linked_list(head)

print(solution.removeNthFromEnd(head, n))
