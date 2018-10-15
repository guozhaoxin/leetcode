#encoding:utf8
__author__ = 'gold'

'''
Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node,node

            rightresult = dfs(node.right)
            leftresult = dfs(node.left)
            if not rightresult:
                node.left = None
                node.right = leftresult[0]
                return node,leftresult[1]
            elif not leftresult:
                return node,rightresult[1]
            else:
                node.left = None
                node.right = leftresult[0]
                leftresult[1].left = None
                leftresult[1].right = rightresult[0]
                return node,rightresult[1]

        dfs(root)

def p(root):
    linked = []
    while root:
        linked.append(root.val)
        root = root.right
    print(linked)


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(5)
    root.left = left
    root.right = right
    leftleft = TreeNode(3)
    leftright = TreeNode(4)
    left.left = leftleft
    left.right = leftright
    rightright = TreeNode(6)
    right.right = rightright
    Solution().flatten(root)
    p(root)