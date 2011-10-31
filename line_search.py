# -*- coding:utf-8 -*-

#列aからbを探す
def lineSearch(a,b):
    for i in a:
        if i==b:
            return True
        else:
            continue
    return False

#テスト
if __name__=='__main__':
    a=[1,2,56,7,9]
    
    print lineSearch(a,3)
    print lineSearch(a,56)

