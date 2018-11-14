#encoding:utf8
__author__ = 'gold'

'''
414. Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        results = [nums[0]]

        for num in nums:

            if len(results) == 3:
                if num <= results[-1] or num == results[0] or num == results[1]:
                    continue

                if num > results[0]:
                    results[2] = results[1]
                    results[1] = results[0]
                    results[0] = num
                    continue

                if num > results[1]:
                    results[2] = results[1]
                    results[1] = num
                    continue

                if num > results[2]:
                    results[2] = num
                    continue

            if len(results) == 2:
                if num == results[0] or num == results[1]:
                    continue

                if num < results[1]:
                    results.append(num)
                    continue

                if num > results[1] and num < results[0]:
                    results.append(results[1])
                    results[1] = num
                    continue

                if num > results[0]:
                    results.append(results[1])
                    results[1] = results[0]
                    results[0] = num
                    continue

            if len(results) == 1:
                if results[0] == num:
                    continue

                if results[0] > num:
                    results.append(num)
                    continue

                if results[0] < num:
                    results.append(results[0])
                    results[0] = num
                    continue

        if len(results) == 3:
            return results[-1]
        else:
            return results[0]

if __name__ == '__main__':
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([2, 2, 3, 1]))