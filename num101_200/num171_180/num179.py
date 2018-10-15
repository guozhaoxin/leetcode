#encoding:utf8
__author__ = 'gold'

'''
Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        import functools

        def compare(a,b):
            index = 0
            while index < len(a) and index < len(b):
                if a[index] > b[index]:
                    return 1
                elif a[index] < b[index]:
                    return -1
                else:
                    index += 1
            if index < len(a):
                while index < len(a) and a[index] == '0':
                    index += 1
                if index == len(a):
                    return -1
                return 1

            if index < len(b):
                while index < len(b) and b[index] == '0':
                    index += 1
                if index == len(b):
                    return 1
                return -1
            return 0

        num2strlist = []
        for num in nums:
            num2strlist.append(str(num))

        print(num2strlist)
        num2strlist.sort(reverse=True,key=functools.cmp_to_key(compare))
        return ''.join(num2strlist) if num2strlist[0] != '0' else '0'

if __name__ == '__main__':
    input = [10,2]
    print(Solution().largestNumber(input))
    print(Solution().largestNumber([3,30,34,5,9]))
    print(Solution().largestNumber([20,1]))
    print(Solution().largestNumber([10,1]))
    print(Solution().largestNumber([1,1,1]))