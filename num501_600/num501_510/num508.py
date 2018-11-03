#encoding:utf8
__author__ = 'gold'

'''
508.
Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
'''

from common.tree import TreeNode

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        subTreeSum = {}
        def dfs(node):
            if not node:
                return 0
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            curSum = node.val + leftSum + rightSum
            if curSum not in subTreeSum:
                subTreeSum[curSum] = 0
            subTreeSum[curSum] += 1
            return curSum
        dfs(root)
        mostFreqSum = 0
        for _,freq in subTreeSum.items():
            if freq > mostFreqSum:
                mostFreqSum = freq

        results = []
        for subSum,freq in subTreeSum.items():
            if freq == mostFreqSum:
                results.append(subSum)
        return results

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-3)
    print(Solution().findFrequentTreeSum(root))