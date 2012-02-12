#! /usr/local/bin/python
# -*- coding:utf-8 -*-

class queue():
    
    def __init__(self,data=[]):
        self.data=data

    def queue_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def enqueue(self,x):
        self.data.append(x)

    def dequeue(self):
        if self.queue_empty():
            print 'queue is empty'
        else:
            result=self.data[0]
            self.data=self.data[1:]
            return result

if __name__=='__main__':
    q=queue()
    q.enqueue(2)
    print q.data
    q.enqueue(3)
    print q.data
    q.dequeue()
    print q.data
    q.dequeue()
    print q.data
    q.dequeue()
    print q.data
