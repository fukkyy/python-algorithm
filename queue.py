# -*- coding:utf-8 -*-

class queue(data=[]):
    
    self.data=data

    def enqueue(self,string):
        self.data.append(string)

    def dequeue(self):
        result=data[0]
        self.data=self.data[1:]
        return result
