#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        self.max = root.val #标记全局最大值

        def dfs(node):
            if not node.left and not node.right:
                if node.val > self.max:
                    self.max = node.val
                return node.val

            if node.val > self.max:
                self.max = node.val

            leftSum = dfs(node.left) if node.left else 0
            rightSum = dfs(node.right) if node.right else 0

            if leftSum + node.val > self.max:
                self.max = leftSum + node.val
            if rightSum + node.val > self.max:
                self.max = rightSum + node.val
            if leftSum + rightSum + node.val > self.max:
                self.max = leftSum + rightSum + node.val

            return max(leftSum + node.val,rightSum + node.val,node.val)

        dfs(root)
        return self.max

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    root = TreeNode(-10)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    righleft = TreeNode(15)
    rightright = TreeNode(7)
    right.left = righleft
    right.right = rightright

    print(Solution().maxPathSum(root))