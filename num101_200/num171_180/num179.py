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

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y: int(y+x)-int(x+y))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ''
        nums = [str(nums[i]) for i in range(len(nums))]
        longest = max([len(x) for x in nums])
        b = [a * longest for a in nums]
        b.sort(reverse=True)
        print(b)
        nums.sort(key=lambda x: x*(longest), reverse=True)
        print(nums)

        if nums and nums[0] == '0':
            return '0'

        for n in nums:
            res = res + n
        return res

if __name__ == '__main__':
    # input = [10,2]
    # print(Solution().largestNumber(input))
    print(Solution().largestNumber([3,30,34,5,9]))
    # print(Solution().largestNumber([20,1]))
    # print(Solution().largestNumber([10,1]))
    # print(Solution().largestNumber([1,1,1]))