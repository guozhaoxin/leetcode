# coding:utf8
__author__ = 'gold'

'''
Let's call an array A a mountain if the following properties hold:
•A.length >= 3
•There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1



Example 2:
Input: [0,2,1,0]
Output: 1

Note:
1.3 <= A.length <= 10000
2.0 <= A[i] <= 10^6
3.A is a mountain, as defined above.

'''


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left < right:
            if A[left] < A[right]:
                left += 1
            elif A[left] == A[right]:
                left += 1
                right -= 1
            else:
                right -= 1
        return left

if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0,2,1,0]))
    print(Solution().peakIndexInMountainArray([0,2,0]))