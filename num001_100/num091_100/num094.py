#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        stack = []

        if not root:
            return results
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            stackTop = stack.pop(-1)
            results.append(stackTop.val)
            cur = stackTop.right

        return results



if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    right = TreeNode(3)
    rightleft = TreeNode(6)
    root.left = left
    root.right = right
    left.left = leftleft
    left.right = leftright
    right.left = rightleft
    results = Solution().inorderTraversal(root)
    print(results)