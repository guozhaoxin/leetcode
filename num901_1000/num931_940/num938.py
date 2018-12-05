#coding:utf8
__author__ = 'gold'

'''
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

 

Note:

    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31.

'''

from common.tree import TreeNode

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int

        """
        if not root:
            return 0

        if root.val < L:
            return self.rangeSumBST(root.right,L,R)

        if root.val > R:
            return self.rangeSumBST(root.left,L,R)

        leftRes = self.rangeSumBST(root.left,L,R)
        rightRes = self.rangeSumBST(root.right,L,R)
        return root.val + leftRes + rightRes

if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)
    root.left = left
    root.right = right
    leftleft = TreeNode(3)
    leftright = TreeNode(7)
    left.left = leftleft
    left.right = leftright
    rightright = TreeNode(18)
    right.right = rightright
    print(Solution().rangeSumBST(root,7,15))