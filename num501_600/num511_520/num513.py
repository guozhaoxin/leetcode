#encoding:utf8
__author__ = 'gold'

'''
513.
Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''

from common.tree import TreeNode

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        parentArray = [root]
        while True:
            childArray = []
            for node in parentArray:
                if node.left:
                    childArray.append(node.left)
                if node.right:
                    childArray.append(node.right)
            if childArray:
                parentArray = childArray
            else:
                return parentArray[0].val