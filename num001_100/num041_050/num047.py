#encoding:utf8
__author__ = 'gold'

'''
Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        if not nums:
            return results
        nums.sort()

        def digui(chosenArray,remaindList):
            '''
            :param chosenArray: list，表示到目前为止已经排序好的数列
            :param remaindList: list，表示还剩下的数列
            :return:
            '''
            if len(remaindList) == 1: #只剩下一个，只要直接将其添加进去即可
                chosenArray.append(remaindList[0])
                results.append(chosenArray)
                return
            else:
                for i in range(len(remaindList)):
                    if i > 0 and remaindList[i] == remaindList[i - 1]:
                        continue
                    newRem = [] #对于每个当前位上选定的数值来说，要得到剩下的数组成的数列
                    for j in range(len(remaindList)):
                        if j != i:
                            newRem.append(remaindList[j])
                    newChosenArray = chosenArray[:] #不能在已经排好序的数列上操作，不然会使得整个数列越来越长
                    newChosenArray.append(remaindList[i])
                    digui(newChosenArray,newRem)

        digui([],nums)

        return results

if __name__ == '__main__':
    numList = [1,1,2,1]
    results = Solution().permute(numList)
    print(len(results))
    print(results)