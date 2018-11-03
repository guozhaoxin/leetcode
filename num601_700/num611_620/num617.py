#encoding:utf8
__author__ = 'gold'

'''
617.
Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
'''
from common.tree import TreeNode
from common.tree import midOrder

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2

        if not t2:
            return t1

        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1

if __name__ == '__main__':
    t1root = TreeNode(1)
    t1left = TreeNode(3)
    t1right = TreeNode(2)
    t1root.left = t1left
    t1root.right = t1right
    t1leftleft = TreeNode(5)
    t1left.left = t1leftleft

    t2root = TreeNode(2)
    t2left = TreeNode(1)
    t2right = TreeNode(3)
    t2root.left = t2left
    t2root.right = t2right
    t2leftright = TreeNode(4)
    t2rightright = TreeNode(7)
    t2left.right = t2leftright
    t2right.right = t2rightright

    t = Solution().mergeTrees(t1root,t2root)
    midOrder(t)