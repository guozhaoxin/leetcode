#encoding:utf8
__author__ = 'gold'

'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return

        i = 1
        tailNode = head
        while i < n and tailNode:
            i += 1
            tailNode = tailNode.next
        if not tailNode:
            return None

        tailNode = tailNode.next
        if not tailNode:
            return head.next
        pre = head
        while tailNode.next:
            pre = pre.next
            tailNode = tailNode.next
        pre.next = pre.next.next
        return head

def p(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    second = ListNode(2)
    # third = ListNode(3)
    # fourth = ListNode(4)
    # fifth = ListNode(5)
    head.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = fifth
    p(head)
    head = Solution().removeNthFromEnd(head,2)
    print('*****')
    p(head)