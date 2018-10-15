#encoding:utf8
__author__ = 'gold'

'''
Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.     
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
          :type head: ListNode
          :type k: int
          :rtype: ListNode
        """
        def revList(node):
            curr, nxt = node, node.next
            while nxt:
                nxtnxt = nxt.next
                nxt.next = curr
                curr, nxt = nxt, nxtnxt
            node.next = None
            return (curr, node)

        prev, curr, c = None, head, 0
        while curr and c < k:
            prev = curr
            curr = curr.next
            c += 1
        if curr == None:
            if c == k: #正好相等可以进行翻转
                return revList(head)[0]
            return head

        temp = curr
        prev.next = None
        newHead, newTail = revList(head)
        newTail.next = self.reverseKGroup(temp, k)
        return newHead


def p(listNode):
    results = []
    while listNode:
        results.append(listNode.val)
        listNode = listNode.next
    print(results)

class Solution(object):
    def reverseKGroup(self, head, k):
        """
          :type head: ListNode
          :type k: int
          :rtype: ListNode
        """
        if not head:
            return head
        if k <= 1 :
            return head

        first = True #标记是否是第一次循环
        beginNode = head

        while beginNode:
            count = 1
            endNode= beginNode
            while endNode and count < k:
                endNode = endNode.next
                count += 1
            if not endNode: #说明本轮不需要转换
                break
            tail = endNode.next #作为下一轮的起点
            thisHead,thisEnd = self.reverse(beginNode,endNode)
            thisEnd.next = tail
            if first:
                head = thisHead
                first = False
                last = thisEnd
            else:
                last.next = thisHead
                last = thisEnd
            beginNode = tail
        return head

    def reverse(self,head,end):
        curNode,nextNode = head,head.next
        while curNode != end:
            nextNodeNext = nextNode.next
            nextNode.next = curNode
            curNode,nextNode = nextNode,nextNodeNext
        return end,head



if __name__ == '__main__':
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(3)
    l1_4 = ListNode(4)
    l1_5 = ListNode(5)
    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5

    head = Solution().reverseKGroup(l1_1,5)
    p(head)