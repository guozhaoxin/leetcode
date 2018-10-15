#encoding:utf8
__author__ = 'gold'

'''
Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''


class Solution1:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        for index in range(len(heights)):
            left = index
            while left >= 0 and heights[left] >= heights[index]:
                left -= 1
            left += 1
            right = index
            while right < len(heights) and heights[index] <= heights[right]:
                right += 1
            right -= 1
            maxArea = max(maxArea,(right - left + 1) * heights[index])

        return maxArea

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        stack = []
        maxArea = 0
        for index in range(len(heights)):
            maxArea = max(maxArea,heights[index])
            if len(stack) == 0 or stack[-1][1] < heights[index]:
                stack.append([index,heights[index]])
                continue
            else:
                while stack and stack[-1][1] >= heights[index]:
                    top = stack[-1]
                    maxArea = max(maxArea,top[1] * (index - top[0]))
                    maxArea = max(maxArea,heights[index] * (index - top[0] + 1))
                    stack.pop()
                stack.append([top[0],heights[index]])

        if stack:
            lastIndex = stack[-1][0]
            while stack:
                ele = stack.pop()
                maxArea = max(maxArea,ele[1] * (len(heights) - ele[0]))

        return maxArea



if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
    print(Solution().largestRectangleArea([1,2,1]))
    print(Solution().largestRectangleArea([1,2,3,4,5,6,7]))
    print(Solution().largestRectangleArea([2,1,2]))
    print(Solution().largestRectangleArea([4,2,0,3,2,5]))
    # print(Solution().largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
    # print(Solution().largestRectangleArea([3,1,4,5,3,2,7,5,3]))
    # print(Solution().largestRectangleArea([3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
    print(Solution().largestRectangleArea([4,4,6,5]))