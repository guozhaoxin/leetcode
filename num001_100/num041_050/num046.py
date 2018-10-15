#encoding:utf8
__author__ = 'gold'

'''
Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        if not nums:
            return results

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
                    newRem = [] #对于每个当前位上选定的数值来说，要得到剩下的数组成的数列
                    for j in range(len(remaindList)):
                        if j != i:
                            newRem.append(remaindList[j])
                    newChosenArray = chosenArray[:] #不能在已经排好序的数列上操作，不然会使得整个数列越来越长
                    newChosenArray.append(remaindList[i])
                    digui(newChosenArray,newRem)

        digui([],nums)

        return results

class Solution1: #这个是别人最快的办法，使用了内部包
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return list(itertools.permutations(nums))

if __name__ == '__main__':
    numList = [i for i in range(30)]
    results = Solution1().permute(numList)
    print(results)
    print(len(results))