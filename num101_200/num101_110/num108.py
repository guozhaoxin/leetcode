#encoding:utf8
__author__ = 'gold'

'''
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        def digui(curroot,startIndex,endIndex,dir):
            if startIndex > endIndex:
                return
            if startIndex == endIndex:
                if dir == 'L':
                    curroot.left = TreeNode(nums[startIndex])
                else:
                    curroot.right = TreeNode(nums[startIndex])
                return
            mid = (startIndex + endIndex) // 2
            newNode = TreeNode(nums[mid])
            if dir == 'L':
                curroot.left = newNode
            else:
                curroot.right = newNode

            digui(newNode,startIndex,mid - 1,'L')
            digui(newNode,mid + 1,endIndex,'R')

        digui(root,0,mid-1,'L')
        digui(root,mid+1,len(nums)-1,'R')
        return root

def pre(root):
    if not root:
        return
    print(root.val)
    pre(root.left)
    pre(root.right)

def mid(root):
    if not root:
        return
    mid(root.left)
    print(root.val)
    mid(root.right)

if __name__ == '__main__':
    s = [-10, -3, 0, 5, 9,10,12]
    s = [i for i in range(20)]
    # s = [1,2,3,4]
    root = Solution().sortedArrayToBST(s)
    pre(root)
    print('****')
    mid(root)