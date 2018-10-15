#encoding:utf8
__author__ = 'gold'

# f = open('what3981.txt','r')
# words3981 = []
# for group in f.readlines():
#     words3981.append(group[:-1])
# f.close()
# print(words3981)
#
# words3982 = []
# f= open('what3982.txt','r')
# for group in f.readlines():
#     words3982.append(group[:-1])
# f.close()
# print(words3982)
#
# temp = []
# for word in words3982:
#     if word not in words3981:
#         temp.append(word)
# print(temp)
#
# temp = []
# for word in words3981:
#     if word not in words3982:
#         temp.append(word)
# print(temp)

a = 'abbbccca'
b = list(a)
print(b)
b.sort()
print(b)
