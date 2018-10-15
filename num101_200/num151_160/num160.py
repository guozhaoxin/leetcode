#encoding:utf8
__author__ = 'gold'

'''
Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        aL = 0 #a链表的长度
        bL = 0 #b链表的长度

        nodeA = headA
        while nodeA:
            aL += 1
            nodeA = nodeA.next

        if not aL:
            return None

        nodeB = headB
        while nodeB:
            bL += 1
            nodeB = nodeB.next

        if not bL:
            return None

        nodeA = headA
        nodeB = headB

        stepDiff = abs(bL - aL)

        if aL > bL:
            culStep = 0
            while culStep != stepDiff:
                culStep += 1
                nodeA = nodeA.next
        elif bL > aL:
            culStep = 0
            while culStep != stepDiff:
                culStep += 1
                nodeB = nodeB.next

        while nodeB != nodeA:
            nodeA = nodeA.next
            nodeB = nodeB.next
            if not nodeA or not  nodeB:
                return None

        return nodeB