#encoding:utf8
__author__ = 'gold'

'''
Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head.next or m == n:
            return head
        tempNode = ListNode(0)
        tempNode.next = head
        last = tempNode
        index = 1
        secondNode = head
        while secondNode and index < m:
            index += 1
            secondNode = secondNode.next
            last = last.next
        if not secondNode:
            return head
        first = secondNode.next
        index += 1
        secondTemp = secondNode
        while first and index <= n:
            temp = first.next
            first.next = secondNode
            secondNode = first
            if index == n:
                break
            if not temp:
                break
            first = temp
            index += 1

        secondTemp.next = temp
        last.next = first
        return tempNode.next


def p(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next

    print(results)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,10]
    nums = [1,2,3,4,5]
    head =  ListNode(0)
    last = head
    for i in nums:
        node = ListNode(i)
        last.next = node
        last = node
    results = Solution().reverseBetween(head.next,1,1)
    results = Solution().reverseBetween(ListNode(5),1,1)
    p(results)