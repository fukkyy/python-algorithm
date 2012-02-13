#! /usr/local/bin/python
# -*- coding:utf-8 -*-

class Linkedlist:
    class cell:
        def __init__(self,key,id,prev=None,next=None):
            self.id=id
            self.key=key
            self.prev=prev
            self.next=next

    def __init__(self,A=[]):
        self.count=1 # var for making cell_id unique
        self.obj=[]
        self.obj.append(self.cell(key='head',id=0,next=None))
        for i in range(len(A)):
            self.insert(A[i],self.count-1,None)

    def list_search(self,x):
        i=0
        while True:
            next=self.obj[i].next
            if next==None:
                break
            obj=self.obj[next]
            if obj.key==x:
                return obj
            i+=1
        return None

    def insert(self,key,prev,next):
        self.obj.append(self.cell(key,self.count,prev,next))
        self.obj[prev].next=self.count
        if next!=None:
            self.obj[next].prev=self.count
        self.count+=1

    def delete(self,key):
        if self.list_search(key)==None:
            print 'input_value doesn\'t exist in list'
        else:
            obj=self.list_search(key)
            self.obj[obj.prev].next=obj.next
            self.obj[obj.next].prev=obj.prev
            self.obj[obj.id].prev=None
            self.obj[obj.id].next=None

if __name__=='__main__':
    ll=linkedlist([1,2])
    ll.insert(5,1,2)
    obj3=ll.obj[3]
    print obj3.key,ll.obj[obj3.prev].key,ll.obj[obj3.next].key #correct->5 1 2
    print ll.list_search(5).key
    ll.delete(5)
    obj1=ll.obj[1]
    print obj1.key,ll.obj[obj1.next].key #correct->1 2
