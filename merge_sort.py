#! /usr/local/bim/python
# -*- coding:utf-8 -*-

import sys

# mergeSort is merge sort function.
# A is array, p is start point and r is end point.
def mergeSort(A,p,r):
    if p<r:
        q=(p+r)/2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    #A: array
    #p,q,r: value of array ,p<=q<r
    n1=q-p+1
    n2=r-q
    L=[0]*(n1+1)
    R=[0]*(n2+1)
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    L[n1]=sys.maxint
    R[n2]=sys.maxint
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

if __name__=='__main__':
    A=[2,14,5,8,7,6,12]
    print 'before sort',A
    mergeSort(A,0,len(A)-1)
    print 'after sort',A
