#encoding:utf8
__author__ = 'gold'

'''
Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        orderList = []
        def haha(node):
            if node:
                haha(node.left)
                orderList.append(node.val)
                haha(node.right)

        haha(root)
        return orderList[k - 1]


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        numList = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                numList.append(p.val)
                if len(numList) == k:
                    return numList[-1]
                p = p.right

        print(numList)

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(1)
    right = TreeNode(4)
    root.left = left
    root.right = right
    leftright = TreeNode(2)
    left.right = leftright
    print(Solution().kthSmallest(root,1))