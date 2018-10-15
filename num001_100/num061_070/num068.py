#encoding:utf8
__author__ = 'gold'

'''
68.
Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        results = []
        leftIndex = 0
        while leftIndex < len(words):
            curL = 0
            rightIndex = leftIndex
            while rightIndex < len(words) and curL + len(words[rightIndex]) + (rightIndex - leftIndex) <= maxWidth:
                curL += len(words[rightIndex])
                rightIndex += 1

            curStr = ''
            if rightIndex - leftIndex == 1 or rightIndex == len(words): #最后一行或者只有一个单词
                curStr += words[leftIndex]
                leftIndex += 1
                while leftIndex < rightIndex:
                    curStr += ' ' + words[leftIndex]
                    leftIndex += 1
                curStr += ' ' * (maxWidth - len(curStr))
            else:
                spaceCount = maxWidth - curL
                if spaceCount % (rightIndex - leftIndex - 1) == 0:
                    spaceC = spaceCount // (rightIndex - leftIndex - 1)
                    curStr += words[leftIndex]
                    leftIndex += 1
                    while leftIndex < rightIndex:
                        curStr += ' ' * spaceC + words[leftIndex]
                        leftIndex += 1
                else:
                    remainder = spaceCount % (rightIndex - leftIndex - 1)
                    spaceC = spaceCount // (rightIndex - leftIndex - 1)
                    curStr += words[leftIndex]
                    leftIndex += 1
                    while remainder > 0:
                        curStr += ' ' * (spaceC + 1) + words[leftIndex]
                        leftIndex += 1
                        remainder -= 1
                    while leftIndex < rightIndex:
                        curStr += ' ' * spaceC + words[leftIndex]
                        leftIndex += 1
            results.append(curStr)

        return results


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    print(Solution().fullJustify(words,maxWidth))

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(Solution().fullJustify(words,maxWidth))

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words,maxWidth))