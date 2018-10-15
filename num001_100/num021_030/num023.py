#encoding:utf8
__author__ = 'gold'

'''
Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoLists(l1, l2):
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

        if not lists:
            return []
        if len(lists) == 1:
            return lists[0]

        while len(lists) != 1:
            head = mergeTwoLists(lists[-1],lists[-2])
            lists.pop()
            lists.pop()
            lists.append(head)

        return lists[0]

from num001_100.num021_030.num021 import p

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        head = ListNode(0)
        curr = head

        listDic = {}
        for i in range(len(lists)):
            if lists[i]:
                listDic[i] = lists[i]

        while len(listDic.keys()) > 1:

            minNum = float('inf')
            minListHead = None
            delKey = None
            for key in listDic.keys():
                if listDic[key].val < minNum:
                    minNum = listDic[key].val
                    minListHead = listDic[key]
                    delKey = key
            curr.next = minListHead
            curr = curr.next
            listDic[delKey] = listDic[delKey].next
            if not listDic[delKey]:
                listDic.pop(delKey)
        if listDic:
            curr.next = listDic[list(listDic.keys())[0]]
        return head.next


if __name__ == '__main__':
    l1_1 = ListNode(1)
    l1_2 = ListNode(4)
    l1_3 = ListNode(5)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3_1 = ListNode(2)
    l3_2 = ListNode(6)
    l3_1.next = l3_2

    head = Solution().mergeKLists([l1_1,l2_1,l3_1])
    head = Solution().mergeKLists([None,None])
    p(head)