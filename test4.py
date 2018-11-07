#encoding:utf8
__author__ = 'gold'

from functools import reduce
a =reduce(lambda x,y:x + y,set([1,2,3]),10)
print(a)
a = reduce(lambda x, y: x * y, range(9, -1, -1), 9)
print(a)