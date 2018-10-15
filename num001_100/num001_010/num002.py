#encoding:utf8
__author__ = 'gold'

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0) #最后要返回的结果
        temp = result
        carry = 0 #表示每一步中计算得到的余数

        while l1 and l2:
            sum = carry + l1.val + l2.val
            if sum >= 10:
                carry = 1
                val = sum - 10
            else:
                carry = 0
                val = sum
            currentNode = ListNode(val)
            temp.next = currentNode
            temp =currentNode
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = carry + l1.val
            if sum >= 10:
                carry = 1
                val = sum - 10
            else:
                carry = 0
                val = sum
            currentNode = ListNode(val)
            temp.next = currentNode
            temp = currentNode
            l1 = l1.next
        while l2:
            sum = carry + l2.val
            if sum >= 10:
                carry = 1
                val = sum - 10
            else:
                carry = 0
                val = sum
            currentNode = ListNode(val)
            temp.next = currentNode
            temp = currentNode
            l2 = l2.next
        if carry != 0:
            temp.next = ListNode(carry)
        return result.next


'''
above is my answer,it worked with low effiency,as the best method on leetcode used
l1 or l2 as the answer space,spared to allocate more space the saved the time 
to allocate the memory. on the other hand, division is slower than subtraction.
'''

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = Solution().addTwoNumbers(l1,l2)
    while l3:
        print(l3.val)
        l3 = l3.next