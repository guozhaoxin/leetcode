#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            topEle = stack.pop()
            res.append(topEle.val)
            for child in (topEle.left,topEle.right):
                if child:
                    stack.append(child)

        res.reverse()
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    right = TreeNode(2)
    rightleft = TreeNode(3)
    root.right = right
    right.left = rightleft
    s = Solution().postorderTraversal(root)
    print(s)