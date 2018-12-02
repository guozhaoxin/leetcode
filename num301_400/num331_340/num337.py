#encoding:utf8
__author__ = 'gold'

'''
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

from common.tree import TreeNode,midOrder

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.dfs(root))

    def dfs(self,node):
        '''
        对传入的节点进行处理计算，找到以该节点为根节点时能得到的最大收益
        :param node: TreeNode,要判断的节点
        :return: tuple(int)，所有可能性
        '''
        if not node.left and not node.right:
            return node.val,0,0

        if not node.right:
            leftResult = self.dfs(node.left)
            return node.val + max(leftResult[1],leftResult[2]),leftResult[0],leftResult[1]

        if not node.left:
            rightResult = self.dfs(node.right)
            return node.val + max(rightResult[1],rightResult[2]),rightResult[0],rightResult[1]

        leftResult = self.dfs(node.left)
        rightResult = self.dfs(node.right)
        return node.val + max(leftResult[1],leftResult[2]) + max(rightResult[1],rightResult[2]),max(leftResult[0],leftResult[1]) + max(rightResult[0],rightResult[1]),leftResult[1] + rightResult[1]


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(4)
    right = TreeNode(5)
    root.left = left
    root.right = right
    leftleft = TreeNode(1) ####
    leftright = TreeNode(3)
    rightright = TreeNode(1)
    left.left = leftleft
    left.right = leftright
    right.right = rightright
    print(Solution().rob(root))

    root = TreeNode(3)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftright = TreeNode(3)
    left.right = leftright
    rightright = TreeNode(1)
    right.right = rightright
    print(Solution().rob(root))

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(Solution().rob(root))

    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)
    print(Solution().rob(root))