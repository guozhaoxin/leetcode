#encoding:utf8
__author__ = 'gold'

'''
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        newHead = ListNode(0)
        newHead.next = head

        currHead = newHead
        left = currHead.next
        right = left.next
        tail = right.next

        while True:
            currHead.next = right
            right.next = left
            left.next = tail

            currHead = currHead.next.next
            left = currHead.next
            if not left:
                break
            right = left.next
            if not right:
                break
            tail = right.next
        return newHead.next


def p(listNode):
    results = []
    while listNode:
        results.append(listNode.val)
        listNode = listNode.next
    print(results)


if __name__ == '__main__':
    l1_1 = ListNode(1)
    l1_2 = ListNode(4)
    l1_3 = ListNode(5)
    l1_4 = ListNode(2)
    # l1_1.next = l1_2
    # l1_2.next = l1_3
    # l1_3.next = l1_4
    head = Solution().swapPairs(l1_1)
    p(head)