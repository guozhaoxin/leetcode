#encoding:utf8
__author__ = 'gold'

'''
Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def p(listNode):
    results = []
    while listNode:
        results.append(listNode.val)
        listNode = listNode.next
    print(results)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1

        if l1 is l2:
            return l1

        currentl1 = l1
        currentl2 = l2

        if l1.val < l2.val:
            head = l1
            currentl1 = l1.next
        else:
            head = l2
            currentl2 = l2.next
        current = head

        while currentl1 and currentl2:
            if currentl1.val < currentl2.val:
                current.next = currentl1
                current = currentl1
                currentl1 = currentl1.next
            else:
                current.next = currentl2
                current = currentl2
                currentl2 = currentl2.next
        if currentl1:
            current.next = currentl1
        if currentl2:
            current.next = currentl2
        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3

    # l = Solution().mergeTwoLists(l1,l2)

    l = Solution().mergeTwoLists(None,None)
    l = Solution().mergeTwoLists(l1,l1)
    p(l)