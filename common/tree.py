#encoding:utf8
__author__ = 'gold'

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def preOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        results.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    print(results)

def midOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        results.append(node.val)
        dfs(node.right)
    dfs(root)
    print(results)

def postOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        results.append(node.val)
    dfs(root)
    print(results)

def arrayToTree(array):
    '''
    将一串array转化成二叉树
    :param array: []
    :return: 根节点，TreeNode类
    '''
    import math
    nodes = []
    index = 0
    while index < len(array):
        print(index)
        if array[index]:
            node = TreeNode(array[index])
            pIndex = math.floor((index - 1) // 2)
            if pIndex >= 0 and pIndex < index:
                if index % 2 == 0:
                    nodes[pIndex].right = node
                else:
                    nodes[pIndex].left = node
        index += 1
    return nodes[0]

if __name__ == '__main__':
    array = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = arrayToTree(array)
    midOrder(root)
