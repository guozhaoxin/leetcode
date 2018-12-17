#encoding:utf8
__author__ = 'gold'

'''
845. Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''


class Solution1:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 3:
            return 0

        stack = []
        mountainLen = 0
        direction = 'up'
        for num in A:
            if not stack:
                direction = 'up'
                stack.append(num)
                continue
            if direction == 'up':
                if num > stack[-1]:
                    stack.append(num)
                elif num == stack[-1]:
                    direction = 'up'
                    stack = [num]
                else:
                    if len(stack) > 1:
                        direction = 'down'
                        stack.append(num)
                    else:
                        direction = 'up'
                        stack = [num]
            else:
                if num < stack[-1]:
                    stack.append(num)
                elif num == stack[-1]:
                    if len(stack) >= 3:
                        mountainLen = max(len(stack),mountainLen)
                    stack = [num]
                    direction = 'up'
                else:
                    if len(stack) >= 3:
                        mountainLen = max(len(stack),mountainLen)
                    temp = stack[-1]
                    stack = [temp,num]
                    direction = 'up'
        if direction == 'down' and len(stack) >= 3:
            mountainLen = max(mountainLen,len(stack))

        return mountainLen

class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 3:
            return 0

        prev = A[0]
        mountainLen = inc = dow = 0
        inc = 1
        for num in A[1:]:
            if num > prev:
                if not dow:
                    inc += 1
                    prev = num
                else:
                    if inc > 1 and inc + dow >= 3:
                        mountainLen = max(mountainLen,inc + dow)
                    inc = 2
                    dow = 0
                    prev = num
            elif num == prev:
                if inc > 1 and dow:
                    if inc + dow >= 3:
                        mountainLen = max(mountainLen,inc + dow)
                inc = 1
                dow = 0
                prev = num
            else:
                if inc == 1:
                    prev = num
                else:
                    dow += 1
                    prev = num
        if inc > 1 and dow:
            mountainLen = max(mountainLen,inc + dow)
        return mountainLen


if __name__ == '__main__':
    print(Solution1().longestMountain([2,1,4,7,3,2,5]))
    print(Solution().longestMountain([2,1,4,7,3,2,5]))
    print(Solution1().longestMountain([2,2,2]))
    print(Solution().longestMountain([2,2,2]))
    print(Solution1().longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
    print(Solution().longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
    print(Solution1().longestMountain([9,8,7,6,5,4,3,2,1,0]))
    print(Solution().longestMountain([9,8,7,6,5,4,3,2,1,0]))
    print(Solution().longestMountain([2,3,3,2,0,2]))
    print(Solution1().longestMountain([2,3,3,2,0,2]))