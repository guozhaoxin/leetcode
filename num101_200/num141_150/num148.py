#encoding:utf8
__author__ = 'gold'

'''
Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        tempList = []
        while head:
            tempList.append(head)
            head = head.next

        tempList.sort(key=lambda x:x.val)
        i = 0
        while i < len(tempList) - 1:
            tempList[i].next = tempList[i + 1]
            i += 1
        tempList[-1].next = None

        return tempList[0]

def p(head):
    results = []
    while head:
        results.append(head.val)
        head = head.next

    print(results)


if __name__ == '__main__':
     import random
     headNode = ListNode(random.randint(-20,20))
     lastNode = headNode
     for i in range(20):
         curNode = ListNode(random.randint(-20,20))
         lastNode.next = curNode
         lastNode = curNode
     p(headNode)
     newHead = Solution().sortList(headNode)
     p(newHead)