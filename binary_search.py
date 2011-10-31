# -*- coding:utf-8 -*-

#列aからbを2分探索法で探してくる
def binarySearch(a,b):
    a.sort()
    while len(a)>0:
        i=int(len(a)/2)
        if a[i]==b:
            return True
        elif a[i]>b:
            a=a[:i]
        else:
            a=a[i+1:]
    return False

#テスト
if __name__=='__main__':
    a=[12,15,19,36,38,45,56,88]
    print binarySearch(a,34)
