#encoding:utf8
__author__ = 'gold'

def eleReplace(array,oriEle,newEle):
    index = 0
    while index < len(array):
        if array[index] == oriEle:
            array[index] = newEle
        index += 1