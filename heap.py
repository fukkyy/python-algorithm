#! /usr/local/bin/python
# -*- coding:utf-8 -*-

class Heap:
    
    def maintain_heapify(self,A,i):
        l=2*i+1
        r=2*i+2
        if self.name=='max':
            if l<len(A) and A[l]>A[i]:
                largest=l
            else:
                largest=i
            
            if r<len(A) and A[r]>A[largest]:
                largest=r
            
            if largest!=i:
                A[largest],A[i]=A[i],A[largest]
                self.maintain_heapify(A,largest)
        elif self.name=='min':
            if l<len(A) and A[l]<A[i]:
                smallest=l
            else:
                smallest=i

            if r<len(A) and A[r]<A[smallest]:
                smallest=r

            if smallest!=i:
                A[smallest],A[i]=A[i],A[smallest]
                self.maintain_heapify(A,smallest)

    def build_heap(self,A):
        i=len(A)/2
        while i>=0:
            self.maintain_heapify(A,i)
            i-=1

    def __init__(self,A,name='max'):
        self.name=name
        self.build_heap(A)
        self.heap=A

    def insert(self,v):
        self.heap.append(v)
        self.build_heap(self.heap)

    def deleteroot(self):
        root=self.heap[:1]
        tmp=self.heap[1:len(self.heap)-1]
        self.heap=self.heap[len(self.heap)-1:]+tmp
        self.build_heap(self.heap)
        return root[0]

    def get_root(self):
        return self.heap[0]

if __name__=='__main__':
    A=[27,17,3,16,13,10,1,5,7,12,4,8,9,0]
    a=Heap(A,'min')
    print a.heap
    a.insert(31)
    print a.heap
    print a.deleteroot()
    print a.heap
    print a.get_root()
    B=[27,17,3,16,13,10,1,5,7,12,4,8,9,0]
    b=Heap(B)
    print b.heap
    b.insert(31)
    print b.heap
    print b.deleteroot()
    print b.heap
    print b.get_root()
