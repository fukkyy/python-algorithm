#! /usr/local/bin/python
# -*- coding:utf-8 -*-

class HashOpenAddress:

    def __init__(self,size=5):
        self.size=size
        self.table=[None]*size
    
    def hash(self,k):
        if type(k)==str:
            return len(k)%self.size
        else:
            return int(k%self.size)
    
    # search hash value for k
    def search_hash(self,k):
        hash=self.hash(k)
        if self.table[hash]==k:
            return hash
        else:
            #search eqaul column
            count=0
            while count<self.size:
                if hash!=self.size-1:
                    hash+=1
                else:
                    hash=0
                if self.table[hash]==k:
                    return hash
                else:
                    count+=1
            if count>=self.size:
                return None

    def insert(self,k):
        hash=self.hash(k)
        if self.table[hash]==None or self.table[hash]=='deleted':
            self.table[hash]=k
        else:
            #searching nil column
            count=0
            while count<self.size:
                #rehush
                if hash!=self.size-1:
                    hash+=1
                else:
                    hash=0
                if self.table[hash]==None or self.table[hash]=='deleted':
                    self.table[hash]=k
                    break
                else:
                    count+=1
            if count>=self.size:
                print 'table is max,no empty colmun'

    def delete(self,k):
        hash=self.search_hash(k)
        if hash!=None:
            self.table[hash]='deleted'
        else:
            print 'no item,so cannot delete'

    def search(self,k):
        hash=self.search_hash(k)
        if hash!=None:
            return self.table[hash]
        else:
            return 'no item'

if __name__=='__main__':
    h=HashOpenAddress()
    print h.table
    h.insert(1)
    print h.table
    h.insert(11)
    print h.table
    h.insert(16)
    print h.table
    h.insert(6)
    print h.table
    h.insert(21)
    print h.table
    h.insert(13)
    print h.search(11)
    h.delete(11)
    print h.table
    print h.search(11)
    h.delete(16)
    print h.table
    h.insert(8)
    print h.table
    print h.search(8)

