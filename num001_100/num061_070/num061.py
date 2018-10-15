#encoding:utf8
__author__ = 'gold'

'''
Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        #先求链表的长度
        linkLen = 1
        node = head
        while node.next:
            linkLen += 1
            node = node.next

        node.next = head
        k %= linkLen
        k = linkLen - k

        node = head
        step = 1
        while step < k:
            node = node.next
            step += 1

        newNead = node.next
        node.next = None
        return newNead

def printLink(head):
    nodeVal = []
    while head:
        nodeVal.append(head.val)
        head = head.next

    print(nodeVal)
if __name__ == '__main__':
    head = ListNode(1)
    temp = head
    for i in range(2,6):
        node = ListNode(i)
        temp.next = node
        temp = node

    head = Solution().rotateRight(head,6)
    printLink(head)