#encoding:utf8
__author__ = 'gold'

'''
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        else:
            leftMinHeight = self.minDepth(root.left) if root.left else float('inf')
            rightMinHeight = self.minDepth(root.right) if root.right else float('inf')
            minHeight = min(leftMinHeight,rightMinHeight)
            return minHeight + 1 if minHeight != float('inf') else 1

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    root.left = left
    # right = TreeNode(3)
    # root.right = right
    # rightright = TreeNode(4)
    # right.right = rightright
    print(Solution().minDepth(root))