#encoding:utf8
__author__ = 'gold'

'''
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''

from common.tree import TreeNode,arrayToTree,midOrder

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        results = []
        if not root or not target:
            return results

        nodeDict = {}
        self.getTreeNodeRelaDic(nodeDict,root,None)

        if target.val not in nodeDict:
            return results

        if K == 0:
            results.append(target.val)
            return results

        if target.left:
            self.dfs(target.left,target.val,K - 1,results,nodeDict)
        if target.right:
            self.dfs(target.right,target.val,K - 1,results,nodeDict)
        if nodeDict[target.val]:
            self.dfs(nodeDict[target.val],target.val,K - 1,results,nodeDict)

        return results

    def getTreeNodeRelaDic(self,nodeDict,root,parent):
        if not root:
            return
        nodeDict[root.val] = parent
        self.getTreeNodeRelaDic(nodeDict,root.left,root)
        self.getTreeNodeRelaDic(nodeDict,root.right,root)

    def dfs(self,node,preVal,step,resultList,nodesDict):
        '''
        dfs to get the results
        :param node: TreeNode,current node to handle
        :param preVal: int,from which node to get here
        :param step: int,remaining distances
        :param resultList: List,the whole results
        :param nodesDict: Dict,the dict to store nodes' relationship
        :return: None
        '''
        if step == 0:
            resultList.append(node.val)
            return
        if node.left and node.left.val != preVal:
            self.dfs(node.left,node.val,step - 1,resultList,nodesDict)
        if node.right and node.right.val != preVal:
            self.dfs(node.right,node.val,step - 1,resultList,nodesDict)
        if nodesDict[node.val] and nodesDict[node.val].val != preVal:
            self.dfs(nodesDict[node.val],node.val,step - 1,resultList,nodesDict)

if __name__ == '__main__':
    null = None
    arrayList = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    root = arrayToTree(arrayList)
    print(Solution().distanceK(root,root.left,2))
    arrayList = [0,1,null,null,2,null,3,null,4]
    root = arrayToTree(arrayList)
    print(Solution().distanceK(root))