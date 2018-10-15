#encoding:utf8
__author__ = 'gold'

'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        heightStack = [] #高度stack

        index = 0
        heightStack.append([index,height[index]])

        waterSize = 0
        index += 1
        while index < len(height) and heightStack:
            while heightStack and heightStack[-1][1] < height[index]:
                curIndex = heightStack[-1][0]
                heightStack.pop()
                if not heightStack:
                    break
                waterSize += (index - heightStack[-1][0] - 1) * (min(height[index],heightStack[-1][1]) - height[curIndex])
            heightStack.append([index,height[index]])
            index += 1

        return waterSize

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [2,1,0,2]
    height = [5] * 5
    print(Solution().trap(height))