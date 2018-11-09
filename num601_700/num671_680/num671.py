#encoding:utf8
__author__ = 'gold'

'''
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''

from common.tree import TreeNode,arrayToTree

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = []

        def dfs(node):
            if not node:
                return
            if not temp:
                temp.append(node.val)
            elif len(temp) == 1 and node.val != temp[0]:
                temp.append(node.val)
                temp.sort()
            elif len(temp) == 2:
                if node.val < temp[0]:
                    temp[1] = temp[0]
                    temp[0] = node.val
                elif temp[0] < node.val and temp[1] > node.val:
                    temp[1] = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if len(temp) < 2:
            return -1
        return temp[-1]

if __name__ == '__main__':
    array = [2,2,5,None,None,5,7]
    root = arrayToTree(array)
    print(Solution().findSecondMinimumValue(root))