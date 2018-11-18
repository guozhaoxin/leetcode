#encoding:utf8
__author__ = 'gold'

'''
343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
'''

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        resultDict = {1:1}

        def dfs(num):
            if num in resultDict:
                return resultDict[num]

            maxProduct = num - 1
            for i in range(2,num // 2 + 1):
                left = dfs(i)
                right = dfs(num - i)
                maxProduct = max(maxProduct,left * right, i * (num - i),i * right,left * (num - i))
            resultDict[num] = maxProduct
            return resultDict[num]
        a = dfs(n)
        return a

if __name__ == '__main__':
    print(Solution().integerBreak(2))
    print(Solution().integerBreak(10))
    print(Solution().integerBreak(8))