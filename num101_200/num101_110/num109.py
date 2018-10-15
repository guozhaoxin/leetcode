#encoding:utf8
__author__ = 'gold'

'''
Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        def digui(curroot, startIndex, endIndex, dir):
            if startIndex > endIndex:
                return
            if startIndex == endIndex:
                if dir == 'L':
                    curroot.left = TreeNode(nums[startIndex])
                else:
                    curroot.right = TreeNode(nums[startIndex])
                return
            mid = (startIndex + endIndex) // 2
            newNode = TreeNode(nums[mid])
            if dir == 'L':
                curroot.left = newNode
            else:
                curroot.right = newNode

            digui(newNode, startIndex, mid - 1, 'L')
            digui(newNode, mid + 1, endIndex, 'R')

        digui(root, 0, mid - 1, 'L')
        digui(root, mid + 1, len(nums) - 1, 'R')
        return root