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

        visitedNodes = [False] * numCourses
        nodeIndex = 0
        while nodeIndex < numCourses:
            if visitedNodes[nodeIndex]:
                nodeIndex += 1
                continue
            nodeStack = []
            nodeSet = set()
            nodeSet.add(nodeIndex)
            nodeStack.append(nodeIndex)
            visitedNodes[nodeIndex] = True
            while nodeStack:
                topNode = nodeStack[-1]
                curNode = 0
                while curNode < numCourses:
                    if graph[topNode][curNode] and curNode in nodeSet:
                        return False
                    if graph[topNode][curNode] == 0: #压根没有连接
                        curNode += 1
                        continue
                    if visitedNodes[curNode] and graph[topNode][curNode] == 1 and curNode in nodeSet:#有连接且访问过且是这条链路上访问过的额
                        return False
                    if graph[topNode][curNode] == 1 and curNode not in nodeSet: #有连接且不在这条链路上
                        if not visitedNodes[curNode]:
                            nodeStack.append(curNode)
                            nodeSet.add(curNode)
                            visitedNodes[curNode] = True
                            break
                        else:
                            curNode += 1
                            continue
                    curNode += 1
                if curNode == numCourses:
                    nodeSet.remove(nodeStack.pop())
            nodeIndex += 1
        return True


if __name__ == '__main__':
    print(Solution().canFinish(2,[[1,0]]))
    print(Solution().canFinish(2,[[0,1]]))
    print(Solution().canFinish(2,[[1,0],[0,1]]))
    print(Solution().canFinish(4,[[0,1],[3,1],[1,3],[3,2]]))