# -*- coding:utf-8 -*-

class stack(data=[]):

    self.data=data

    def push(self,input_data):
        self.data.append(input_data)

    def pop(self):
        num=len(self.data)-1
        result=self.data[num]
        self.data=self.data[0:num]
        return result
