#encoding:utf8
__author__ = 'gold'

'''

'''

def haha(n):
    result = [1]
    if n == 1:
        return result

    left = 0
    while len(result) < n:
        temp = result[-1]
        temp *= 2
