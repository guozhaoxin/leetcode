#encoding:utf8
__author__ = 'gold'

'''
Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None

        meet = None
        slow = head
        fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                meet = slow
                break
        if not meet:
            return
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next