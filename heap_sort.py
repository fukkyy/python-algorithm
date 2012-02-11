#! /usr/local/bin/pyhton
# -*- coding:utf-8 -*-

# To maintain heap condition
# input A:array, i:node number
def max_heapify(A,i):
    l=2*i+1
    r=2*i+2
    if l<len(A) and A[l]>A[i]:
        largest=l
    else:
        largest=i
    
    if r<len(A) and A[r]>A[largest]:
        largest=r
    
    if largest!=i:
        A[largest],A[i]=A[i],A[largest]
        max_heapify(A,largest)

# To build heap structure
def build_max_heap(A):
    i=len(A)/2
    while i>=0:
        max_heapify(A,i)
        i-=1

# Do heapsort
def heapsort(A):
    result=[]
    build_max_heap(A)
    while len(A)>1:
        result.append(A[0])
        tmp=A[1:len(A)-1]
        A=A[len(A)-1:]
        A=A+tmp
        build_max_heap(A)
    return result

if __name__=="__main__":
    A=[27,17,3,16,13,10,1,5,7,12,4,8,9,0,31]
    result=heapsort(A)
    print result
