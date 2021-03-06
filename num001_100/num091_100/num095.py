#encoding:utf8
__author__ = 'gold'

'''
Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        self.ht = {}

        return self.generateTreesHelper(1, n)

    def generateTreesHelper(self, i, j):
        if i > j:
            return [None]

        if (i, j) in self.ht:
            return self.ht[(i, j)]

        tmp = []
        for k in range(i, j + 1):
            l = self.generateTreesHelper(i, k - 1)
            r = self.generateTreesHelper(k + 1, j)
            for l_i in l:
                for r_i in r:
                    root = TreeNode(k)
                    root.left = l_i
                    root.right = r_i
                    tmp.append(root)

        self.ht[(i, j)] = tmp

        return tmp


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        tree_list = [[[None]] * (n + 2) for i in range(n + 2)]
        for i in range(1, n + 1):
            tree_list[i][i] = [TreeNode(i)]
            for j in range(i - 1, 0, -1):
                tree_list[j][i] = []
                for k in range(j, i + 1):
                    for left in tree_list[j][k - 1]:
                        for right in tree_list[k + 1][i]:
                            root = TreeNode(k)
                            (root.left, root.right) = (left, right)
                            tree_list[j][i].append(root)
        return tree_list[1][n]