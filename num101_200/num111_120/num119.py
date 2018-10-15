#encoding:utf8
__author__ = 'gold'

'''
Pascal's Triangle II
 
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space? 
'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        results = [1 for i in range(rowIndex + 1)]

        if rowIndex <= 1:
            return results

        rowIndex += 1

        for row in range(2,rowIndex):
            for index in range(1,row):
                if index == 1:
                    temp = results[index]
                    results[index] += results[index - 1]
                else:
                    temp2 = results[index]
                    results[index] += temp
                    temp = temp2

        return results

if __name__ == '__main__':
    results = Solution().getRow(3)
    print(results)