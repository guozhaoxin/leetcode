#encoding:utf8
__author__ = 'gold'

nums = ['1','2','3','4','5']
results = []

def digui(res:int,index:int) ->int:
    if index == len(nums) - 1:
        results.append(res.append(nums[index]))
    else:
        pass

def digui(b,i):
    if i != 0:
        b[i] = i
        digui(b,i - 1)
    else:
        return


a = set()
for i in range(2 ** 10):
    a.add(i)

for i in range(1**10):
    a.remove(i)