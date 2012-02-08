#! /usr/local/bin/python
# -*- coding:utf-8 -*-

def fizzbuzz(num):
    if num%3==0 and num%5==0:
        res='FizzBuzz'
    elif num%3==0:
        res='Fizz'
    elif num%5==0:
        res='Buzz'
    else:
        res=num
    return res

def print_fizzbuzz(end):
    for i in range(1,end+1):
        print fizzbuzz(i)

if __name__=='__main__':
    print_fizzbuzz(16)
