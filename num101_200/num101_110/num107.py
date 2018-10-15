#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if not root:
            return results

        nodeStack = [] #存储每一层节点
        nodeStack.append(root)
        while nodeStack:
            tempStack = []
            tempVal = []
            for node in nodeStack:
                tempVal.append(node.val)
                if node.left:
                    tempStack.append(node.left)
                if node.right:
                    tempStack.append(node.right)
            nodeStack = tempStack
            results.append(tempVal)

        return results[::-1]

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

    print(Solution().levelOrderBottom(root))
