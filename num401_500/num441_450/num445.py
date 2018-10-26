#encoding:utf8
__author__ = 'gold'

'''
445.
Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1List = []
        while l1:
            l1List.append(l1.val)
            l1 = l1.next
        l2List = []
        while l2:
            l2List.append(l2.val)
            l2 = l2.next

        l1List.reverse()
        l2List.reverse()

        result = []
        remainder = 0
        index = 0
        while index < len(l1List) and index < len(l2List):
            curSum = remainder + l1List[index] + l2List[index]
            result.append(curSum % 10)
            remainder = curSum // 10
            index += 1

        if index < len(l1List):
            while index < len(l1List):
                curSum = remainder + l1List[index]
                result.append(curSum % 10)
                remainder = curSum // 10
                index += 1
        if index < len(l2List):
            while index < len(l2List):
                curSum = remainder + l2List[index]
                result.append(curSum % 10)
                remainder = curSum // 10
                index += 1

        if remainder == 1:
            result.append(1)

        index = len(result) - 1
        temp = ListNode(1)
        previous = temp
        while index >= 0:
            curNode = ListNode(result[index])
            previous.next = curNode
            previous = curNode
            index -= 1
        return temp.next

def createLinked(numList):
    temp = ListNode(0)
    previous = temp
    for num in numList:
        tempNode = ListNode(num)
        previous.next = tempNode
        previous = tempNode
    return temp.next

def scanLinked(l):
    header = l
    result = []
    while header:
        result.append(header.val)
        header = header.next
    print(result)

if __name__ == '__main__':
    l1 = createLinked([7,2,4,3])
    l2 = createLinked([5,6,4])
    scanLinked(l1)
    scanLinked(l2)
    result = Solution().addTwoNumbers(l1,l2)
    scanLinked(result)