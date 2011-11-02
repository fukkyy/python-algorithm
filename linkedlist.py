class linkedlist:
    class cell:
        def __init__(self,data,link=None):
            self.data=data
            self.link=link

    def __init__(self,*args):
        self.top=linkedlist.cell(None)
        for x reversed(args):
            self.insert(0,x)

    def insert(self,data,link):
        pass

    def delete(self,data,link):
        pass
