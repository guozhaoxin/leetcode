#encoding:utf8
__author__ = 'gold'

'''
701.
Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
'''

from common.tree import TreeNode

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        parent = None
        node = root
        while node:
            if node.val == val:
                return root
            if node.val < val:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left

        if parent.val < val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)

        return root