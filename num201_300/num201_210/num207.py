#encoding:utf8
__author__ = 'gold'

'''
207.
Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[0] * numCourses for i in range(numCourses)]
        for pair in prerequisites:
            cour0 = pair[0]
            cour1 = pair[1]
            graph[cour0][cour1] = 1

        visited = [ False for i in range(numCourses)]
        for index in range(numCourses):
            if visited[index] == True:
                continue
            for col in range(numCourses):
                if graph[index][col] == 1:
                    break
            else:
                visited[index] = True
                continue
            visSet = set()
            stack = []
            stack.append(index)
            visSet.add(index)
            visited[index] = True
            nextIndex = index
            while stack:
                nextIndex = self.__helper(graph,nextIndex,visSet,numCourses)
                if nextIndex == -1:
                    return False
                if nextIndex == numCourses:
                    # stack.pop()
                    visSet.remove(stack.pop())
                    continue
                visited[nextIndex] = True
                visSet.add(nextIndex)
                stack.append(nextIndex)

        return True

    def __helper(self,graph,row,visSet,numCourses):
        col = 0
        while col < numCourses:
            if graph[row][col] == 1 and col not in visSet:
                visSet.add(col)
                return col
            elif graph[row][col] == 1 and col in visSet:
                return -1
            col += 1
        return col


# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         graph = [[0] * numCourses for i in range(numCourses)]
#         for pair in prerequisites:
#             cour0 = pair[0]
#             cour1 = pair[1]
#             graph[cour0][cour1] = 1



if __name__ == '__main__':
    print(Solution().canFinish(2,[[1,0]]))
    # print(Solution().canFinish(2,[[1,0],[0,1]]))