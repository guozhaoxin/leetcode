#encoding:utf8
__author__ = 'gold'

import multiprocessing
import time

def func(msg):
    print("msg:", msg)
    time.sleep(3)
    print("end")

if __name__ == "__main__":
    from collections import defaultdict

    frequencies = defaultdict(int)  # 传入int()函数来初始化
    for word in ['a','b']:
        frequencies[word] += 1
    print(frequencies)