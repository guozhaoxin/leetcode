#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        frontier = [root]
        while frontier:
            expand = frontier.pop()
            res.append(expand.val)
            for child in [expand.right, expand.left]:
                if child:
                    frontier.append(child)
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    right = TreeNode(2)
    rightleft = TreeNode(3)
    root.right = right
    right.left = rightleft
    res = Solution().preorderTraversal(root)
    print(res)