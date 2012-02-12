#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def bubble_sort(A):
    n=len(A)
    for i in range(n):
        for j in range(n-1-i):
            if A[n-1-j]<A[n-2-j]:
                A[n-1-j],A[n-2-j]=A[n-2-j],A[n-1-j]
    return A


if __name__=='__main__':
    A=[18,35,76,23,49,42,31,12]
    print 'before sort:'
    print A
    print 'after sort:'
    print bubble_sort(A)
