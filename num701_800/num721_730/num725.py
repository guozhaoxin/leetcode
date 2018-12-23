#encoding:utf8
__author__ = 'gold'

'''
725. Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:

Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:

Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:
The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
'''


from common.node.listNode import ListNode

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: listNode
        :type k: int
        :rtype: List[ListNode]
        """

        if not root:
            return [[] for i in range(k)]

        node = root
        listLen = 0
        while node:
            listLen += 1
            node = node.next

        aveLen = listLen // k
        partsLenArray = [aveLen for i in range(k)]
        step = listLen % k
        for i in range(step):
            partsLenArray[i] += 1

        res = []
        node = root
        for i in range(k):
            curL = partsLenArray[i]
            if curL == 0:
                res.append(None)
                continue

            step = 1
            res.append(node)
            while step <= curL:
                previous = node
                node = node.next
                step += 1
            previous.next = None

        return res

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
    # array = [1,2,3]
    # array = [1,2,3,4]
    root = ListNode.array2list(array)
    res = Solution().splitListToParts(root,5)
    print(res)
    for ele in res:
        ans = []
        if ele:
            node = ele
            while node:
                ans.append(node.val)
                node = node.next
        print(ans)
