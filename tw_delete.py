#! /usr/local/bin/python
# -*- coding:utf-8 -*-

import twitter
import sys
import time

consumer_key='Your Consumer Key'
consumer_secret='Your Consumer Secret'
token='Your Access Token Key'
token_secret='Your Access Token Secret'

def set_api():
    return twitter.Api(consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=token,
            access_token_secret=token_secret)

#最新のtweet3200個のidを取得
def get_tweet_id():
    tw_api=set_api()

    count=200
    max_id=None

    id_list=[]
    i=0

    while True:
        if i==16:
            break
        i+=1
        try:
            data=tw_api.GetUserTimeline(count=count,max_id=max_id,include_rts=True)
            for s in data:
                if max_id!=s.id:
                    id_list.append(s.id)
                max_id=s.id
            print "get_tweet_id%s回目" % i
        except:
            print "get_tweet_id%s回目" % i
            print sys.exc_info()
            break
    return id_list

#渡されたtweetのidのリストを展開してtweetを削除
def tweet_delete(id_list):
    tw_api=set_api()
    for id in id_list:
        try:
            data=tw_api.DestroyStatus(id)
            print "delete id:%s,tweet:%s" % (data.id,data.text)
        except:
            print sys.exc_info()
            continue

if __name__=='__main__':
    id_list=get_tweet_id()
    tweet_delete(id_list)
