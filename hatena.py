#! /usr/local/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import json

# HatenaApi Class makes calling Hatena Api easy.
class HatenaApi:
    
    # when you make instance, you need url parameter.
    # contsructer sets property count(int),scrrenshot(str),title(str),bookmarks(list) 
    def __init__(self,url):
        api_url='http://b.hatena.ne.jp/entry/jsonlite/'
        params=urllib.urlencode({'url':url})
        f=urllib2.urlopen(api_url+'?'+params)
        data=json.loads(f.read())

        if data!=None:
            self.count=int(data['count'])
            self.screenshot=data['screenshot']
            self.title=data['title']
            self.bookmarks=data['bookmarks']
        else:
            self.count=0
            self.screenshot=''
            self.title=''
            self.bookmarks=[]
    # get_tags() function return tag data(type:dictionary)
    # dictionary's key is tag name and value is tag count.
    def get_tags(self):
        tags={}
        if len(self.bookmarks)!=0:
            for b in self.bookmarks:
                for tag in b['tags']:
                    tags.setdefault(tag,0)
                    tags[tag]+=1
        return tags
