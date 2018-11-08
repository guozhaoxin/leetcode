#encoding:utf8
__author__ = 'gold'


class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


def preOrder(root,printed = False):
    '''
    preorder the binary tree
    :param root: TreeNode，the root node of the binary tree
    :param printed:bool,print the order result or not
    :return: [],contain the order element value
    '''
    results = []
    def dfs(node):
        if not node:
            return
        results.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    if printed:
        print(results)
    return results


def midOrder(root,printed = False):
    '''
    midorder the binary tree
    :param root: TreeNode，the root node of the binary tree
    :param printed:bool,print the order result or not
    :return: [],contain the order element value
    '''
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        results.append(node.val)
        dfs(node.right)
    dfs(root)
    if printed:
        print(results)
    return results


def postOrder(root,printed = False):
    '''
    postorder the binary tree
    :param root: TreeNode，the root node of the binary tree
    :param printed:bool,print the order result or not
    :return: [],contain the order element value
    '''
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        results.append(node.val)
    dfs(root)
    if printed:
        print(results)
    return results

def arrayToTree(array):
    '''
    translate an array to a binary tree
    :param array: []
    :return: TreeNode,a new tree root node
    '''

    if not array or array[0] is None:
        return None

    nodes = [TreeNode(array[0])]
    index = 1
    try:
        while index < len(array):
            if array[index] is not None:
                node = TreeNode(array[index])
                nodes.append(node)
                pIndex = (index - 1) // 2
                if index % 2:
                    nodes[pIndex].left = node
                else:
                    nodes[pIndex].right = node
            else:
                nodes.append(None)
            index += 1
    except AttributeError as e:
        print('the array is wrong!')
        return None
    return nodes[0]


if __name__ == '__main__':
    array = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = arrayToTree(array)
    print(root.val)
    midOrder(root,True)
    postOrder(root,True)
    preOrder(root,True)
