#encoding:utf8
__author__ = 'gold'

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        num_alp_dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        def digui(index):
            if index == len(digits) - 1:
                return num_alp_dic[digits[-1]]
            results = digui(index + 1)
            curr_results = []
            for char in num_alp_dic[digits[index]]:
                for str in results:
                    str = char + str
                    curr_results.append(str)
            return curr_results
        results = digui(0)
        return results

if __name__ == '__main__':
    print(Solution().letterCombinations('2'))
    print(Solution().letterCombinations('23'))
    print(Solution().letterCombinations('8'))
