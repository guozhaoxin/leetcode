#encoding:utf8
__author__ = 'gold'

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.name = name

    def run(self):
        for i in range(5):
            print(threading.currentThread().name,i)
            print(threading.currentThread().isAlive())
            time.sleep(0.5)


# import threading
# import time
#
# condition = threading.Condition()
# products = 0
#
# class Producer(threading.Thread):
#     def run(self):
#         global products
#         while True:
#             if condition.acquire():
#                 if products < 10:
#                     products += 1;
#                     print("Producer(%s):deliver one, now products:%s" %(self.name, products))
#                     condition.notify()#不释放锁定，因此需要下面一句
#                     condition.release()
#                 else:
#                     print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products))
#                     condition.wait();#自动释放锁定
#                 time.sleep(2)
#             else:
#                 print('线程没有拿到锁')
#
# class Consumer(threading.Thread):
#     def run(self):
#         global products
#         while True:
#             if condition.acquire():
#                 if products > 1:
#                     products -= 1
#                     print("Consumer(%s):consume one, now products:%s" %(self.name, products))
#                     condition.notify()
#                     condition.release()
#                 else:
#                     print("Consumer(%s):only 1, stop consume, products:%s" %(self.name, products))
#                     condition.wait();
#                 time.sleep(2)
#             else:
#                 print('这里也没有拿到锁！')
#
# if __name__ == "__main__":
#     for p in range(0, 2):
#         p = Producer()
#         p.start()
#
#     for c in range(0, 3):
#         c = Consumer()
#         c.start()

import multiprocessing
import time

def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.daemon = True
    p.start()
    print ("p.pid:", p.pid)
    print ("p.name:", p.name)
    print ("p.is_alive:", p.is_alive())