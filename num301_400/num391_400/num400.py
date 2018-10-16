#encoding:utf8
__author__ = 'gold'

'''
400.
Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
'''


class Solution(object):
    # num one digit: 1 * 9, num two digits: 2 * 90, etc.
    nums = [i * 9 * (10 ** (i - 1)) for i in range(10)]

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find how many digits the last number falls into
        i = 1
        while i < len(self.nums):
            if self.nums[i] == n:
                return 9
            if self.nums[i] > n:
                break
            n -= self.nums[i]
            i += 1

        # need to move these many numbers forward
        counter = n // i
        # then move these many digits forward
        remainder = n % i
        # starting from this number
        start = 10 ** (i - 1) + counter

        # if remainder is 0, then it falls into the last digit in the previous number
        if remainder == 0:
            return (start - 1) % 10

        # pick the right digit (index starts with 0)
        return int(str(start)[remainder - 1])

