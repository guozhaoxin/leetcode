#encoding:utf8
__author__ = 'gold'

'''
812.
Largest Triangle Area

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        if len(points) < 3:
            return 0
        if len(points) == 3:
            return self.triangleArea(points[0],points[1],points[2])
        maxArea = 0
        for left in range(0,len(points) - 2):
            for middle in range(left + 1,len(points) - 1):
                for right in range(middle + 1,len(points)):
                    area = self.triangleArea(points[left], points[middle], points[right])
                    maxArea = max(maxArea,area)

        return maxArea


    def triangleArea(self,pointA,pointB,pointC):
        ABsize = ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**.5
        ACsize = ((pointA[0] - pointC[0])**2 + (pointA[1] - pointC[1])**2)**.5
        BCsize = ((pointB[0] - pointC[0])**2 + (pointB[1] - pointC[1])**2)**.5
        p = (ABsize + ACsize + BCsize) / 2
        area = (p * (p - ABsize) * (p - ACsize) * (p - BCsize))**.5
        if type(area) is float:
            return area
        return 0

if __name__ == '__main__':
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    points = [[9,7],[6,10],[1,10],[2,7]]
    points = [[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]
    print(Solution().largestTriangleArea(points))