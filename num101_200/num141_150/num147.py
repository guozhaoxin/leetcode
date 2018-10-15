#encoding:utf8
__author__ = 'gold'

'''
Insertion Sort List

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        cur = head.next
        previous = head
        while cur:
            haha = head
            hahapre = None
            while haha.val < cur.val:
                hahapre = haha
                haha = haha.next
            if haha.val == cur.val and haha is cur:
                previous = cur
                cur = cur.next
            else:
                previous.next = cur.next
                if not hahapre:
                    cur.next = head
                    head = cur
                else:
                    hahapre.next = cur
                    cur.next = haha
                cur = previous.next
        return head

def p(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next

    print(l)

if __name__ == '__main__':
    import random
    head = ListNode(0)
    temp = head
    for i in range(10):
        node = ListNode(random.randrange(20))
        temp.next = node
        temp = node
    p(head.next)
    node = Solution().insertionSortList(head.next)
    p(node)