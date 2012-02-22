#! /usr/local/bin
# -*- coding:utf-8 -*-

def grep(file,query):
    count=0
    n=len(query)
    answer=[]
    for f in open(file,'r'):
        #大文字小文字変換
        f.lower()
        for word in f:
            if word==query[count]:
                count+=1
                if count==n:
                    count=0
                    answer.append(f)
            else:
                count=0
    return answer



if __name__=='__main__':
    query='hoge'
    answer=grep('./test.txt',query)
    for a in answer:
        print a
