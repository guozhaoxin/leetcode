#encoding:utf8
__author__ = 'gold'

'''
Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

from common.print_linked import pLink

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        indictor = (len(stack) + 1) // 2

        node = head
        while len(stack) >= indictor:
            topE = stack.pop()
            tempNode = node.next
            node.next = topE
            topE.next = tempNode
            node = node.next.next
        node.next = None

if __name__ == '__main__':
    head = ListNode(None)
    pre = head
    for i in range(10):
        cur = ListNode(i + 1)
        pre.next = cur
        pre = cur
    pLink(head.next)
    Solution().reorderList(head.next)
    pLink(head.next)
    node = ListNode(1)
    Solution().reorderList(node)
    pLink(node)
