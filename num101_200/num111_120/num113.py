#encoding:utf8
__author__ = 'gold'

'''
Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        results = []
        if not root:
            return results

        def dfs(node,remainder,preList):

            if not node.left and not node.right:
                if remainder == node.val:
                    preList.append(remainder)
                    results.append(preList)
                return
            if node.left:
                dfs(node.left,remainder - node.val,preList + [node.val])
            if node.right:
                dfs(node.right,remainder - node.val,preList + [node.val])

        dfs(root,sum,[])
        return results

def p(root):
    results = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        results.append(node.val)
        dfs(node.right)
    dfs(root)
    print(results)

if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(4)
    right = TreeNode(8)
    root.left = left
    root.right = right
    leftleft = TreeNode(11)
    left.left = leftleft
    leftleftleft = TreeNode(7)
    leftleftright = TreeNode(2)
    leftleft.left = leftleftleft
    leftleft.right = leftleftright
    rightleft = TreeNode(13)
    rightright = TreeNode(4)
    right.left = rightleft
    right.right = rightright
    rightrightleft = TreeNode(5)
    rightrightright = TreeNode(1)
    rightright.left = rightrightleft
    rightright.right = rightrightright

    root = TreeNode(-2)
    right = TreeNode(-3)
    root.right = right

    p(root)

    results = Solution().pathSum(root,-5)
    print(results)