#encoding:utf8
__author__ = 'gold'

'''
Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        index = len(digits) - 1
        temDigit = digits[index] + 1
        if temDigit < 10:
            digits[index] = temDigit
        else:
            digits[index] = temDigit - 10
            carry = 1
            index -= 1
            while index > -1:
                temDigit = digits[index] + carry
                if temDigit < 10:
                    digits[index] = temDigit
                    carry = 0
                    break
                else:
                    digits[index] = temDigit - 10
                    carry = 1
                    index -= 1
            if carry != 0:
                digits.insert(0,1)

        return digits

if __name__ == '__main__':
    input = [4,3,2,1]
    print(Solution().plusOne(input))