#encoding:utf8
__author__ = 'gold'

'''
572.
Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

from common.tree import TreeNode

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s and t:
            return False
        if s and not t:
            return False
        if s.val != t.val:
            return False


    def helper(self,nodes, nodet):
        if not nodes and not nodet:
            return True
        if nodes and not nodet:
            return False
        if not nodes and nodet:
            return False
        if nodes.val != nodet.val:
            return False
        return self.helper(nodes.left, nodet.left) and self.helper(nodes.right, nodet.right)



if __name__ == '__main__':
    s = TreeNode(3)
    left = TreeNode(4)
    right = TreeNode(5)
    s.left = left
    s.right = right
    leftleft = TreeNode(1)
    leftright = TreeNode(2)
    left.left = leftleft
    left.right = leftright
    leftrightleft = TreeNode(0)
    # leftright.left = leftrightleft
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print(Solution().isSubtree(s,t))
    s = TreeNode(1)
    s.left = TreeNode(1)
    t = TreeNode(1)
    print(Solution().isSubtree(s,t))

    s = TreeNode(1)
    s.left = TreeNode(2)
    s.right = TreeNode(3)
    t = TreeNode(1)
    t.left = TreeNode(2)
    print(Solution().isSubtree(s,t))