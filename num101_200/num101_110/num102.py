#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        results = []
        if not root:
            return results

        fifo = []
        fifo.append(root)
        fifo.append(None)

        curLevelList = []
        curIndex = 0
        while True:
            if fifo[curIndex]:
                curLevelList.append(fifo[curIndex].val)
                if fifo[curIndex].left:
                    fifo.append(fifo[curIndex].left)
                if fifo[curIndex].right:
                    fifo.append(fifo[curIndex].right)
            else:
                results.append(curLevelList)
                if curIndex == len(fifo) - 1:
                    break
                curLevelList = []
                fifo.append(None)

            curIndex += 1

        return results

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
    results = Solution().levelOrder(root)
    print(results)