#encoding:utf8
__author__ = 'gold'

'''
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        previous = head
        cur = head.next

        while cur:
            if previous.val == cur.val:
                previous.next = cur.next
                cur = cur.next
            else:
                previous = cur
                cur = cur.next
        return head

def p(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next
    print(results)

if __name__ == '__main__':
    head = ListNode(1)
    next = ListNode(1)
    head.next = next
    next2 = ListNode(2)
    next.next = next2
    next = ListNode(3)
    next2.next = next
    next2 = ListNode(3)
    next.next = next2
    Solution().deleteDuplicates(head)
    p(head)