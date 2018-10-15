#encoding:utf8
__author__ = 'gold'

'''
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        curStack = [] #标记当前轮的情况
        curStack.append(root)

        while True:
            leftStack = [] #下一轮左边的子节点
            rightStack = [] #下一轮右边的子节点
            index = 0
            while index <= len(curStack) // 2:
                leftNode = curStack[index]
                rightNode = curStack[len(curStack) - 1 - index]
                if (leftNode and (not rightNode)) or ((not leftNode) and rightNode):
                    return False
                if (not leftNode) and (not rightNode):
                    leftStack.append(None)
                    rightStack.append(None)
                else:
                    if leftNode.val != rightNode.val:
                        return False
                    leftStack.append(leftNode.left)
                    leftStack.append(leftNode.right)
                    rightStack.append(rightNode.right)
                    rightStack.append(rightNode.left)
                index += 1
            while rightStack:
                leftStack.append(rightStack.pop())
            curStack = leftStack
            for node in curStack:
                if node:
                    break
            else:
                return True
        return True


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        curStack = [] #标记当前轮的情况
        curStack.append(root)

        def digui(left,right):
            if ((not left) and right) or (left and (not right)):
                return False
            if (not left) and (not right):
                return True
            if left.val != right.val:
                return False
            return digui(left.left,right.right) and digui(left.right,right.left)

        return digui(root.left,root.right)


if __name__ == '__main__':
    p = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(2)
    p.left = left
    p.right = right
    leftLeft = TreeNode(3)
    leftRight = TreeNode(4)
    rightLeft = TreeNode(4)
    rightRight = TreeNode(3)
    left.left = leftLeft
    left.right = leftRight
    right.left = rightLeft
    right.right = rightRight

    print(Solution().isSymmetric(p))