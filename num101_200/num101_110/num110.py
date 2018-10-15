#encoding:utf8
__author__ = 'gold'

'''
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(node):
            if not node:
                return [0,True]
            leftBal = dfs(node.left)
            rightBal = dfs(node.right)
            if not leftBal[1] or not rightBal[1] or abs(leftBal[0] - rightBal[0]) > 1:
                return [0,False]
            else:
                return [max(leftBal[0],rightBal[0]) + 1,True]

        return dfs(root)[1]

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    rightleft = TreeNode(15)
    rightright = TreeNode(7)
    right.left = rightleft
    right.right = rightright
    print(Solution().isBalanced(root))