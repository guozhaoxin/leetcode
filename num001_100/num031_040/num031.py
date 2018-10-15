#encoding:utf8
__author__ = 'gold'

'''
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) == 1:
            return

        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                lastIndex = len(nums) - 1
                while lastIndex >= index:
                    if nums[lastIndex] > nums[index - 1]:
                        break
                    lastIndex -= 1
                nums[index-1],nums[lastIndex] = nums[lastIndex],nums[index-1]
                print(lastIndex,index)
                self.resort(index,nums)
                return
            else:
                index -= 1

        if index == 0:
            self.resort(0,nums)

    def resort(self,startIndex,nums):
        mid = startIndex + ((len(nums)) - startIndex) // 2
        newL = int(2 * (startIndex + (len(nums) - startIndex - 1) / 2 ))
        index = startIndex
        while index < mid:
            temp = newL - index
            nums[index],nums[temp] = nums[temp],nums[index]
            index += 1


if __name__ == '__main__':
    nums = [6,5,4,3,2,1]
    nums = [1,4,5,3,2]
    Solution().nextPermutation(nums)
    print(nums)