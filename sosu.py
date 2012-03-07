#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def check_sosu(num):
    if num==1:
        return False
    flag=0
    #素数かどうかの判定
    i=2
    while True:
        if i>=num:
            break
        if num%i==0:
            flag=1
            break
        else:
            i+=1
    if flag==0:
        return True
    else:
        return False

def count_sosu(default=1000):
    import time
    num=2
    for i in range(default):
        if check_sosu(num):
            print num
            time.sleep(0.5)
        num+=1
