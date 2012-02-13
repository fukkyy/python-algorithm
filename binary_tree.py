# -*- coding:utf-8 -*-
    
class BinaryTree:

    class Node:
        def __init__(self,key,id,parent=None,left=None,right=None):
            self.key=key
            self.id=id
            self.parent=parent
            self.left=left
            self.right=right

    def __init__(self,A=[]):
        self.count=1 #var for making Node id unique
        self.node=[]
        # data[0] is dummy node. It shows tree's start
        # and tree's root is Node.right.
        self.node.append(self.Node('start',0))
        for i in A:
            self.insert(i)

    def search_node_id(self,k):
        node_id=self.node[0].right
        #searching node_id
        while True:
            if node_id==None:
                return None

            if k==self.node[node_id].key:
                return node_id
            elif k<self.node[node_id].key:
                node_id=self.node[node_id].left
            else:
                node_id=self.node[node_id].right

    def search(self,k):
        node_id=self.search_node_id(k)
        if node_id==None:
            return 'no node'
        else:
            return self.node[node_id].key

    def insert(self,k):
        # first insert
        if self.node[0].right==None:
            self.node.append(self.Node(k,self.count,0))
            self.node[0].right=self.count
            self.count+=1
        else:
            #searching insert point
            node_id=self.node[0].right
            while True:
                if k<=self.node[node_id].key:
                    if self.node[node_id].left==None:
                        self.node.append(self.Node(k,self.count,node_id))
                        self.node[node_id].left=self.count
                        self.count+=1
                        break
                    else:
                        node_id=self.node[node_id].left
                else:
                    if self.node[node_id].right==None:
                        self.node.append(self.Node(k,self.count,node_id))
                        self.node[node_id].right=self.count
                        self.count+=1
                        break
                    else:
                        node_id=self.node[node_id].right


    def delete(self,k):
        delete_id=self.search_node_id(k)
        if delete_id==None:
            print 'no node'
            return None
        else:
            delete_node=self.node[delete_id]
        # no child
        if delete_node.left==None and delete_node.right==None:
            if delete_node.key<=self.node[delete_node.parent].key:
                self.node[delete_node.parent].left=None
            else:
                self.node[delete_node.parent].right=None
        #one child
        elif delete_node.left==None or delete_node.right==None:
            if delete_node.key<=self.node[delete_node.parent].key:
                if delete_node.left!=None:
                    self.node[delete_node.parent].left=delete_node.left
                else:
                    self.node[delete_node.parent].left=delete_node.right
            else:
                if delete_node.left!=None:
                    self.node[delete_node.parent].right=delete_node.left
                else:
                    self.node[delet_node.parent].right=delete_node.right
        #two child
        else:
            #searching cover node
            min_node=self.node[self.node[delete_node.id].left]
            while True:
                if min_node.left==None:
                    break
                min_node=self.node[self.node[min_node.id].left]
            # changing node pointer
            if min_node.parent==delete_node.id:
                min_node.parent=delete_node.parent
                min_node.right=delete_node.right
                if delete_node.right!=None:
                    self.node[delete_node.right].parent=min_node.id

                if min_node.key<=self.node[delete_node.parent].key:
                    self.node[delete_node.parent].left=min_node.id
                else:
                    self.node[delete_node.parent].right=min_node.id
            else:
                self.node[min_node.parent].left=min_node.right
                self.node[min_node.right].parent=min_node.parent
                min_node.parent=delete_node.parent
                min_node.left=delete_node.left
                min_node.right=delete_node.right
                self.node[delete_node.left].parent=min_node.id
                if delete_node.right!=None:
                    self.node[delete_node.right].parent=min_node.id

                if min_node.key<=self.node[delete_node.parent].key:
                    self.node[delete_node.parent].left=min_node.id
                else:
                    self.node[delete_node.parent].right=min_node.id

if __name__=='__main__':
    bt=BinaryTree()
    A=[34,51,72,17,66]
    print bt.search(34)
    for i in A:
        bt.insert(i)
    bt.insert(81)
    bt.insert(57)
    bt.insert(62)
    print bt.search(17)
    print bt.search(30)
    print bt.search(72)
    print bt.search(62)
    bt.delete(72)
    print bt.search(57)
    print bt.search(66)
    print bt.search(72)
    print bt.search(81)
    bt.delete(81)
    print bt.search(81)
