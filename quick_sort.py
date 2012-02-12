#! /usr/local/bin/python
# -*-coding:utf-8 -*-

# A:list,p:start point,r:end point
# how to use:calling "quick_sort(A,0,len(A)-1)"
def quick_sort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quick_sort(A,p,q)
        quick_sort(A,q+1,r)

# partition devides list(over pivot and under pivot)
# return: number of  under pivot point 
def partition(A,p,r):
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i

if __name__=='__main__':
    A=[2,8,7,1,3,5,6,4]
    quick_sort(A,0,len(A)-1)
    print A
