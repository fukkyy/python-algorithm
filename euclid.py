# coding -*- coding:utf-8 -*-

#mとnの最大公約数を求める(m>n)
def euclid(m,n):
    while True:
        r=m%n
        if r==0:
            return n
        else:
            m=n
            n=r


#テスト
if __name__=='__main__':
    print euclid(3425,1233)
