#encoding:utf8
__author__ = 'gold'

'''
264.
Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [1,2,3]
        if n <= 3:
            return results[:n][-1]
        l1 = [0,[5]]
        l2 = [1,[2,3,5]]
        l3 = [2,[2,3,5]]

        while len(results) < n:
            first = results[l1[0]] * l1[1][0]
            second = results[l2[0]] * l2[1][0]
            third = results[l3[0]] * l3[1][0]
            haha = min(first,second,third)
            results.append(haha)
            if first == haha:
                del l1[1][0]
                if len(l1[1]) == 0:
                    l1 = [max(l1[0],l2[0],l3[0]) + 1,[2,3,5]]
                    while results[l1[0]] * l1[1][0] <= haha:
                        del l1[1][0]
            if second == haha:
                del l2[1][0]
                if len(l2[1]) == 0:
                    l2 = [max(l1[0],l2[0],l3[0]) + 1,[2,3,5]]
                    while results[l2[0]] * l2[1][0] <= haha:
                        del l2[1][0]

            if third == haha:
                del l3[1][0]
                if len(l3[1]) == 0:
                    l3 = [max(l1[0],l2[0],l3[0]) + 1,[2,3,5]]
                    while results[l3[0]] * l3[1][0] <= haha:
                        del l3[1][0]

        return results[-1]

if __name__ == '__main__':
    print(Solution().nthUglyNumber(12))