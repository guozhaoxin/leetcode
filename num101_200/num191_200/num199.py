#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        results = []
        if not root:
            return results

        stack = [root]
        results.append(root.val)
        while stack:
            child = []
            for node in stack:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if not child:
                break
            results.append(child[-1].val)
            stack = child

        return results

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftright = TreeNode(5)
    rightright = TreeNode(4)
    left.right = leftright
    right.right = rightright
    print(Solution().rightSideView(root))