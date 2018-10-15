#encoding:utf8
__author__ = 'gold'

'''
Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

from common.tree import midOrder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return None,None
            if node.left:
                node.left.right,node.left.left = dfs(node.left)
            if node.right:
                node.right.right,node.right.left = dfs(node.right)
            return node.left,node.right
        if not root:
            return
        root.right,root.left = dfs(root)
        return root

if __name__ == '__main__':
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(7)
    root.left = left
    root.right = right
    leftleft = TreeNode(1)
    leftright = TreeNode(3)
    left.left = leftleft
    left.right = leftright
    rightleft = TreeNode(6)
    rightright = TreeNode(9)
    right.left = rightleft
    right.right = rightright
    midOrder(root)
    root = Solution().invertTree(root)
    midOrder(root)
    midOrder(Solution().invertTree(None))