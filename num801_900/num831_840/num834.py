#encoding:utf8
__author__ = 'gold'

'''
834. Sum of Distances in Tree

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000
'''

import collections


class Solution:
    def sumOfDistancesInTree(self, N, edges):
        dic1 = collections.defaultdict(list)
        for e in edges:
            dic1[e[0]].append(e[1])
            dic1[e[1]].append(e[0])


        # eachItem subtreeDist[n]=[a, b] means subtree rooted at n has totally a nodes,
        # and sum of distance in the subtree for n is b
        subtreeDist = [[0, 0] for _ in range(N)]

        ans = [0] * N

        def sumSubtreeDist(n, exclude):
            cnt, ret = 0, 0
            exclude.add(n)
            for x in dic1[n]:
                if x in exclude:
                    continue
                res = sumSubtreeDist(x, exclude)
                cnt += res[0]
                ret += (res[0] + res[1])
            subtreeDist[n][0] = cnt + 1
            subtreeDist[n][1] = ret
            return cnt + 1, ret

        # recursively calculate the sumDist for all subtrees
        # 0 can be replaced with any other number in [0, N-1]
        # and the chosen root has its correct sum distance in the whole tree
        sumSubtreeDist(0, set())

        # visit and calculates the sum distance in the whole tree
        def visit(n, pre, exclude):
            if pre == -1:
                ans[n] = subtreeDist[n][1]
            else:
                ans[n] = ans[pre] - 2 * subtreeDist[n][0] + N
            exclude.add(n)
            for x in dic1[n]:
                if x not in exclude:
                    visit(x, n, exclude)
        print(subtreeDist)
        visit(0, -1, set())
        return ans



if __name__ == '__main__':
    print(Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    # print(Solution().sumOfDistancesInTree(N = 4, edges = [[0,1],[0,2],[1,3]]))