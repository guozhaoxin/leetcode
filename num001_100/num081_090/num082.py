#encoding:utf8
__author__ = 'gold'

'''
Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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

        if not head or not head.next:
            return head

        temp = ListNode('打倒美帝')

        curNode = head
        last = temp

        while curNode:
            LinkedNextN = curNode.next
            if not LinkedNextN:
                last.next = curNode
                break
            while LinkedNextN and LinkedNextN.val == curNode.val:
                LinkedNextN = LinkedNextN.next
            if LinkedNextN is curNode.next:
                last.next = curNode
                last = curNode
                curNode = curNode.next
                last.next = None
            else:
                curNode = LinkedNextN

        return temp.next

def pLinked(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next
    print(results)

if __name__ == '__main__':
    nums = [1,1,1,2,3]
    head = ListNode(1)
    temp = head
    for i in nums:
        node = ListNode(i)
        temp.next = node
        temp = node
    pLinked(head.next)
    p = Solution().deleteDuplicates(head.next)
    pLinked(p)