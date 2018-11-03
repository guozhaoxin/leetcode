#encoding:utf8
__author__ = 'gold'

'''
515.
Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        results = []
        parentArray = [root]
        while parentArray:
            largestVal = parentArray[0].val
            childArray = []
            for node in parentArray:
                if node.left:
                    childArray.append(node.left)
                if node.right:
                    childArray.append(node.right)
                if node.val > largestVal:
                    largestVal = node.val
            results.append(largestVal)
            if not childArray:
                return results
            parentArray = childArray