#encoding:utf8
__author__ = 'gold'

'''
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         self.head = head
#         def dfs(node):
#             if not node.next:
#                 self.head = node
#                 return node
#             else:
#                 newTail = dfs(node.next)
#                 newTail.next = node
#                 node.next = None
#                 return node
#
#         if not head:
#             return
#
#         dfs(head)
#         return self.head


def p(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


if __name__ == '__main__':
    head = ListNode(0)
    temp = head
    for i in range(1,10):
        node = ListNode(i)
        temp.next = node
        temp = node

    p(head)
    head = Solution().reverseList(head)
    p(head)