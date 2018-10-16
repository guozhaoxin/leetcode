#encoding:utf8
__author__ = 'gold'

'''
274.
H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "
A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers 
have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse = True)
        index = len(citations) - 1
        while index >= 0:
            if index + 1 <= citations[index]:
                return index + 1
            index -= 1
        return 0

if __name__ == '__main__':
    print(Solution().hIndex([3,0,6,1,5]))
    print(Solution().hIndex([5,5,4,3,3,1,1,0]))