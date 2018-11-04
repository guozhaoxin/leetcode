#encoding:utf8
__author__ = 'gold'

'''
654.
Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''

from common.tree import TreeNode,midOrder

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        def dfs(left,right):
            if left < 0 or left >= len(nums) or left > right:
                return

            index = left
            maxIndex = left
            while index <= right:
                if nums[index] > nums[maxIndex]:
                    maxIndex = index
                index += 1
            node = TreeNode(nums[maxIndex])
            node.left = dfs(left,maxIndex - 1)
            node.right = dfs(maxIndex + 1,right)
            return node
        return dfs(0,len(nums) - 1)

if __name__ == '__main__':
    root = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
    midOrder(root)
    root = Solution().constructMaximumBinaryTree([])
    midOrder(root)