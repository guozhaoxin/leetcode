#encoding:utf8
__author__ = 'gold'

'''
Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        treeCount = [1 for i in range(n + 1)]
        treeCount[2] = 2
        nums = [i + 1 for i in range(n)]

        for i in range(3,n + 1):
            count = 0
            for j in range(0,i):
                count += treeCount[j] * treeCount[i - j - 1]
            treeCount[i] = count

        return treeCount[n]

if __name__ == '__main__':
    print(Solution().numTrees(5))