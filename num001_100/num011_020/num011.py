#encoding:utf8
__author__ = 'gold'

'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0 #最大面积

        leftIndex = 0
        rightIndex = len(height) - 1
        while leftIndex < rightIndex:
            area = min(height[leftIndex],height[rightIndex]) * (rightIndex - leftIndex)
            if area > maxArea:
                maxArea = area
            if height[leftIndex] > height[rightIndex]:
                rightIndex -= 1
            elif height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            else:
                leftIndex += 1
                rightIndex -= 1

        return maxArea
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))