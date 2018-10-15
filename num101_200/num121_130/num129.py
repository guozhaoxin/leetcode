#encoding:utf8
__author__ = 'gold'

'''
Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.sum = 0

        def dfs(node,culSum):
            if not node:
                return
            if not node.left and not node.right:
                self.sum += culSum * 10 + node.val
                return
            if node.left:
                dfs(node.left,culSum * 10 + node.val)
            if node.right:
                dfs(node.right,culSum * 10 + node.val)

        dfs(root,0)
        return self.sum
if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    rightleft = TreeNode(15)
    rightright = TreeNode(7)
    right.left = rightleft
    right.right = rightright
    # print(Solution().sumNumbers(root))

    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print(Solution().sumNumbers(root))
    print(Solution().sumNumbers(None))