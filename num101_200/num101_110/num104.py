#encoding:utf8
__author__ = 'gold'

'''
 Maximum Depth of Binary Tree
 
 Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(1)
    # left = TreeNode(2)
    # right = TreeNode(3)
    # root.left = left
    # root.right = right
    print(Solution().maxDepth(root))