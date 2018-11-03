#encoding:utf8
__author__ = 'gold'

'''
543.
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

from common.tree import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            leftDiameter = dfs(node.left)
            rightDiameter = dfs(node.right)
            self.diameter = max(self.diameter,leftDiameter + rightDiameter)
            return max(leftDiameter,rightDiameter) + 1
        dfs(root)
        return self.diameter

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    left.left = leftleft
    left.right = leftright
    print(Solution().diameterOfBinaryTree(root))