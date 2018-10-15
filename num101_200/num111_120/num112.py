#encoding:utf8
__author__ = 'gold'

'''
Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        def digui(node,cursum):
            if not node:
                return False

            if not node.left and not node.right:
                return cursum + node.val == sum

            return digui(node.left,cursum + node.val) or digui(node.right,cursum + node.val)

        return digui(root,0)


if __name__ == '__main__':
    root = TreeNode(5)

    left = TreeNode(4)
    right = TreeNode(8)
    root.left = left
    root.right = right
    leftleft = TreeNode(11)
    left.left = leftleft
    rightleft = TreeNode(13)
    rightright = TreeNode(4)
    right.left = rightleft
    right.right = rightright
    leftleftleft = TreeNode(7)
    leftleftright = TreeNode(2)
    leftleft.left = leftleftleft
    leftleft.right = leftleftright
    rightrightright = TreeNode(1)
    rightright.right = rightrightright

    print(Solution().hasPathSum(root,28))