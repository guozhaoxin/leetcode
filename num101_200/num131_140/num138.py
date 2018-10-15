#encoding:utf8
__author__ = 'gold'

'''
Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return

        pre = RandomListNode('zjj')

        pointDic = {}
        step = -1
        while head:
            cur = RandomListNode(head.label)
            cur.random = head.random
            head = head.next
            pre.next = cur
            pre = cur
        pre.next = None

        head = pre.next
        while head:
            if head.random:
                temp = pre.next
                while temp and temp is not head.random:
                    temp = temp.next