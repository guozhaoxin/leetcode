#encoding:utf8
__author__ = 'gold'

'''
894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20
'''

from common.tree import TreeNode

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """

        results = []

        if N <= 0 or N == 2:
            return results

        if N == 1:
            results.append(TreeNode(0))
            return results

        if N == 3:
            root = TreeNode(0)
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            results.append(root)
            return results
        n = N
        for i in range(1, n // 2 + 1):
            leftNodes = i
            rightNodes = n - 1 - i
            leftResult = self.allPossibleFBT(leftNodes)
            if not leftResult:
                continue
            rightResult = self.allPossibleFBT(rightNodes)
            if not rightResult:
                continue
            for left in leftResult:
                for right in rightResult:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    results.append(root)
                    if leftNodes == rightNodes:
                        continue
                    root = TreeNode(0)
                    root.left = right
                    root.right = left
                    results.append(root)
        return results

if __name__ == '__main__':
    result = Solution().allPossibleFBT(7)
    print(result)
    print(len(result))

    result = Solution().allPossibleFBT(19)
    print(result)
    print(len(result))