#encoding:utf8
__author__ = 'gold'

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return True

        step = 0
        cur = head
        while cur:
            step += 1
            cur = cur.next

        l = (step - 1) // 2
        step = 0
        cur = head
        while step <= l:
            cur = cur.next
            step += 1

        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        newHead = pre
        while newHead and head:
            if newHead.val != head.val:
                return False
            newHead = newHead.next
            head = head.next

        return True

def p(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == '__main__':
    head = ListNode(1)
    second = ListNode(2)
    head.next = second
    third = ListNode(1)
    second.next = third
    fourth = ListNode(1)
    # third.next = fourth
    # third = ListNode(2)
    # second.next = third
    # fourth = ListNode(1)
    # fifth = ListNode(3)
    # fourth.next = fifth
    # third.next = fourth
    print(Solution().isPalindrome(head))