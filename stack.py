#! /usr/local/bin/python
# -*- coding:utf-8 -*-


class stack:

    def __init__(self,data=[]):
        self.data=data
    
    def stack_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def push(self,x):
        self.data.append(x)

    def pop(self):
        if self.stack_empty():
            print 'stack is empty'
        else:
            num=len(self.data)-1
            result=self.data[num]
            self.data=self.data[0:num]
            return result

if __name__=='__main__':
    s=stack()
    s.push(2)
    print s.data
    s.push(3)
    print s.data
    s.pop()
    print s.data
    s.pop()
    print s.data
    s.pop()
    print s.data
