#encoding:utf8
__author__ = 'gold'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def array2list(cls,array):
        if not array:
            return None

        root = ListNode(array[0])
        previous = root
        for i in range(1,len(array)):
            cur = ListNode(array[i])
            previous.next = cur
            previous = cur
        return root

    @classmethod
    def printList(cls,root):
        if not root:
            return []

        res = []
        while root:
            res.append(root.val)
            root = root.next

        return res