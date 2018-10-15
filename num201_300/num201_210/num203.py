#encoding:utf8
__author__ = 'gold'

'''
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        tempHead = ListNode(0)
        tempHead.next = head
        pre = tempHead
        cur = pre.next

        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next

        return tempHead.next