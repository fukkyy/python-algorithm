# -*- coding:utf-8 -*-
    
class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None

def search(node,x):
    while node:
        if node.data==x:
            return True
            
        if x<node.data:
            node=node.left

        else:
            node=node.right
        
    return False

def insert(node,x):
    if node is None:
        return Node(x)
    elif x==node.data:
        return node
    elif x<node.data:
        node.left=insert(node.left,x)
    else:
        node.right=insert(node.right,x)
    
    return node

def delete(node,x):
    pass
