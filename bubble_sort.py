# -*- coding:utf-8 -*-

def bubbleSort(array):
    n=len(array)
    for i in range(0,n-1):
        j=n-1
        while j>0:
            if array[j]<array[j-1]:
                n1=array[j]
                n2=array[j-1]
                array[j]=n2
                array[j-1]=n1
            j-=1
            if j==i:
                break
    return array

if __name__=='__main__':
    array=[18,35,76,23,49,42,31,12]
    print 'before sort:'
    print array
    print 'after sort:'
    print bubbleSort(array)
