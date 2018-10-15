#encoding:utf8
__author__ = 'gold'

def pLink(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)