#encoding:utf8
__author__ = 'gold'

'''
848. Shifting Letters

We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
'''


class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """


        shiftCounts = [0] * len(S)
        # for i in range(len(shiftCounts)):
        #     shiftCounts[i] = ord(S[i]) - 97

        totalShiftTounts = 0
        for i in range(len(shifts) - 1,-1,-1):
            totalShiftTounts += shifts[i]
            shiftCounts[i] = totalShiftTounts

        for i in range(len(shifts)):
            shiftCounts[i] = chr((ord(S[i]) - 97 + shiftCounts[i])% 26 + 97)

        return ''.join(shiftCounts)

if __name__ == '__main__':
    print(Solution().shiftingLetters(S = "abc", shifts = [3,5,9]))
    print(Solution().shiftingLetters(S = "z", shifts = [1]))
