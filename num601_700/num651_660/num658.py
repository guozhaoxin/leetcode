#encoding:utf8
__author__ = 'gold'


'''
658. Find K Closest Elements

 Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104

'''


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        return sorted(sorted(arr, key=lambda num: (abs(num - x), num))[:k])


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[len(arr) - k:len(arr)]

        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if abs(x - arr[mid]) > abs(x - arr[mid + k]):
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

if __name__ == '__main__':
    print(Solution().findClosestElements([1,2,3,4,5], k=4, x=-1))
    print(Solution().findClosestElements([1,2,3,5,8,13,21,34], k=3, x=6))
    print(Solution().findClosestElements([1,2,3,4,5], k=4, x=3))