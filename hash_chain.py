#! /usr/local/bin/python
# -*- coding:utf-8 -*-

import linkedlist

class HashChain:
    
    def __init__(self,size=5):
        self.size=size # size is table size
        self.table=[]
        for i in range(size):
            obj=linkedlist.Linkedlist()
            self.table.append(obj)

    # hash function returns k mod 5(int)
    # k: string
    def hash(self,k):
        if type(k)==str:
            return len(k)%self.size
        else:
            return int(k%5)

    def insert(self,k):
        hash=self.hash(k)
        #search end point
        next_id=0
        pre_id=0
        while True:
            next_id=self.table[hash].obj[next_id].next
            if next_id==None:
                end_id=self.table[hash].obj[pre_id].id
                break
            else:
                pre_id=next_id
        self.table[hash].insert(k,end_id,None)

    def delete(self,k):
        hash=self.hash(k)
        self.table[hash].delete(k)

    def search(self,k):
        hash=self.hash(k)
        #serach id
        search_obj=self.table[hash].list_search(k)
        if search_obj==None:
            return 'no item'
        else:
            return self.table[hash].obj[search_obj.id].key

if __name__=='__main__':
    h=HashChain()
    print h.table[4].obj[0].next
    h.insert(4)
    h.insert(5)
    h.insert('poko')
    print h.search(4)
    print h.search(0)
    print h.search('poko')
    h.delete('poko')
    print h.search('poko')
