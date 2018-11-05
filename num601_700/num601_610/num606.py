#encoding:utf8
__author__ = 'gold'

'''
606.
Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''

from common.tree import TreeNode

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s = ''
        if t:
            s += str(t.val)
            if not t.left and not t.right:
                return s
            if t.left and t.right:
                return s + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
            if t.left:
                return s + '(' + self.tree2str(t.left) + ')'
            return s + '()(' + self.tree2str(t.right) + ')'
        return s

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    print(Solution().tree2str(root))