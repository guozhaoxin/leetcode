#encoding:utf8
__author__ = 'gold'

'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
'''

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #先处理A包含B
        if A <= E and B <= F and C >= G and D >= H:
            return (C - A) * (D - B)

        #处理B包含A
        if A >= E and B >= F and C <= G and D <= H:
            return (G - E) * (H - F)

        #处理A B不相交
        if C <= E or A >= G:
            return (C - A) * (D - B) + (G - E) * (H - F)

        #处理相交
        areaA = (C - A) * (D - B)
        areaB = (G - E) * (H - F)
        areaSum = areaA + areaB
        if E <= C <= G:
            if F <= D <= H:
                return areaSum - (C - E) * (D - F)
            else:
                return areaSum - (H - B) * (C - E)
        else:
            if F <= D <= H:
                return areaSum - (D - F) * (G - A)
            else:
                return areaSum - (G - A) * (H - B)

    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        return (A - C) * (B - D) + (E - G) * (F - H) - overlap

if __name__ == '__main__':
    print(Solution().computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))
    print(Solution().computeArea(-2,-2,2,2,-3,1,-1,3))
    print(Solution().computeArea(-2,-2,2,2,-3,-3,3,-1))