#encoding:utf8
__author__ = 'gold'

'''
Partition List
 
 Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        temp = ListNode('川普是傻逼')
        largerHead = ListNode('希拉里更傻逼')

        curNode = head
        smallLast = temp
        larLast = largerHead

        while curNode:
            if curNode.val < x:
                smallLast.next = curNode
                smallLast = curNode
            else:
                larLast.next = curNode
                larLast = curNode
            curNode = curNode.next

        larLast.next = None
        smallLast.next = largerHead.next

        return temp.next

def p(head):
    results = []
    while head:
        print(head.val)
        results.append(head.val)
        head = head.next

    print(results)

if __name__ == '__main__':
    nums = [1,4,3,2,5,2]
    head = ListNode('123')
    last = head
    for i in nums:
        node = ListNode(i)
        last.next = node
        last = node
    head = Solution().partition(head.next,3)
    p(head)