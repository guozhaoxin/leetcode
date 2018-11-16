#encoding:utf8
__author__ = 'gold'

'''
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 1:
            return S
        if len(S) == 2:
            if S[1] != S[0]:
                return S
            return ''

        charDict = {}
        for char in S:
            if char not in charDict:
                charDict[char] = 0
            charDict[char] += 1

        charList = [None for _ in range(len(S))]
        for index in range(len(charList)):
            char = None
            maxCount = 0
            for item in charDict:
                if charDict[item] > maxCount and (index == 0 or item != charList[index - 1]):
                    maxCount = charDict[item]
                    char = item
            if maxCount == 0:
                return ''
            charList[index] = char
            charDict[char] -= 1

        return ''.join(charList)


if __name__ == '__main__':
    # print(Solution().reorganizeString('aba'))
    # print(Solution().reorganizeString('aaab'))
    # print(Solution().reorganizeString("vvvlo"))
    # print(Solution().reorganizeString("ogccckcwmbmxtsbmozli"))
    s = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
    print(len(s))
    result = Solution().reorganizeString(s)
    print(result)
    print(len(s))