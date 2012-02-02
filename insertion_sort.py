#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def insertion_sort(array):
    result=[]
    result.append(array[0])

    for j in range(1,len(array)):
        key=array[j]
        result.append(key)
        i=j-1
        while i>=0 and key<result[i]:
            result[i+1]=result[i]
            result[i]=key
            i-=1
    return result

if __name__=="__main__":
    array=[5,2,4,6,1,3]
    print insertion_sort(array)
