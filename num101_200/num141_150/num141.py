#encoding:utf8
__author__ = 'gold'

'''
Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        backPoint = head
        frontPoint = head

        while backPoint and frontPoint:
            if backPoint.next:
                backPoint = backPoint.next
            else:
                return False

            if frontPoint.next and frontPoint.next.next:
                frontPoint = frontPoint.next.next
            else:
                return False

            if backPoint == frontPoint :
                return True
