#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        results = []
        if not root:
            return results

        fifo = [] #
        fifo.append(root)
        fifo.append(None)
        startIndex = 0
        endIndex = 1
        direction = 1

        while True:
            curList = []
            if startIndex == endIndex:
                break

            for index in range(startIndex,endIndex):
                curList.append(fifo[index].val)
                if fifo[index].left:
                        fifo.append(fifo[index].left)
                if fifo[index].right:
                    fifo.append(fifo[index].right)
            fifo.append(None)
            startIndex = endIndex + 1
            endIndex = startIndex
            while fifo[endIndex]:
                endIndex += 1
            if direction == -1:
                curList.reverse()
            results.append(curList)
            direction = -direction

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
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    rightleft = TreeNode(15)
    rightright = TreeNode(7)
    right.left = rightleft
    right.right = rightright

    # root = TreeNode(1)
    # left = TreeNode(2)
    # right = TreeNode(3)
    # root.left = left
    # root.right = right
    # leftleft = TreeNode(4)
    # left.left = leftleft
    # rightright = TreeNode(5)
    # right.right = rightright

    p(root)
    results = Solution().zigzagLevelOrder(root)
    print(results)