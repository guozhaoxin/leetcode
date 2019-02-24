#coding: utf-8
__author__ = 'gold'
__date__ = '2019/2/24'
__time__ = '10:03'
__filename__ = 'num378.py'

'''
378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
'''


'''
below class can work correctly,but too many puzzles.
'''
class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start + 1 < end:
            mid = (start + end) // 2
            count = self.countLessEqual(matrix,mid)
            if count < k:
                start = mid
            else:
                end = mid
        if self.countLessEqual(matrix,start) >= k:
            return start
        return end

    def countLessEqual(self,matrix,val):
        j = count = 0
        i = len(matrix) - 1
        while i >= 0 and j < len(matrix[0]):
            if(matrix[i][j]) <= val:
                j += 1
                count += i + 1
            else:
                i -= 1

        return count


class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        l = matrix[0][0]
        r = matrix[-1][-1]

        def upper_bound(row, x):
            l = 0
            r = len(row)
            while l < r:
                m = l + (r - l) // 2
                if row[m] > x:
                    r = m
                else:
                    l = m + 1
            return l

        while l < r:
            m = l + (r - l) // 2
            total = 0
            for row in matrix:
                total += upper_bound(row, m)
            if total >= k:
                r = m
            else:
                l = m + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest(matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,))