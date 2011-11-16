# -*-coding:utf-8 -*-
def quickSort(array,i,j):
    '''
    高速な配列のソート
    '''
    pivot=find_pivot(array,i,j)
    k=partition(array,i,j,pivot)
    quickSort(array,i,k-1)
    quickSort(array,k,j)

def find_pivot(array,i,j):
    '''
    arrayのiからj番目を探索
    異なる2つの値を得た時点で大きい方を返す
    '''
    x=i
    while True:
        if x+1==j:
            return array[x]
        if array[x]==array[x+1]:
            continue
        elif array[x]>array[x+1]:
            return array[x]
        else:
            return array[x+1]

def partition(array,l,r,pivot):
    '''
    arrayのi-j番目の要素の順番を入れ替える
    k番目まではpivotより小さく,k番目以降はpivotより大きい
    '''
    while True:
        while array[l]<pivot:
            l=l+1
        while array[r]>=pivot:
            r=r-1
        if l>r:
            return l
        tmp_l=array[l]
        tmp_r=array[r]

        array[r]=tmp_l
        array[l]=tmp_r
