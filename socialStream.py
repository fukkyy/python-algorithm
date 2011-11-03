# -*- coding:utf-8 -*-

class socialStream:
    
    #facebookのlikeのurlを取得
    #params access_token:facebookのアクセストークン,num:取得したいurlの数
    #return urlのリスト
    def getLikeToUrl(self,access_token,num):
        import facebook
        import json

        facebook_app_id='Your faecbook app id'
        facebook_app_secret='Your facebook app secret'

        url_list=[]
        graph=facebook.GraphAPI(access_token)
        url_like_list=graph.fql("SELECT url FROM url_like WHERE user_id = me() LIMIT "+str(num))
        for url_like_dict in url_like_list:
            url_list.append(url_like_dict["url"])
        return url_list
    
    #facebookのshareのurlを取得
    #params access_token:facebookのアクセストークン、num:取得したいurlの数
    #return urlのリスト
    def getShareToUrl(self,access_token,num):
        import facebook
        import json
        
        url_list=[]
        graph=facebook.GraphAPI(access_token)
        url_share_link=graph.fql("SELECT url FROM link WHERE owner = me() LIMIT" + str(num))
        for url_share_dict in url_share_list:
            url_list.append(url_like_dict["url"])
        return url_list
    
    #はてなのidからはてぶしているurlを取得
    #params user_name:はてなid,num:取得したいurlの数
    #return urlのリスト
    def getHatebFromUser(self,user_name,num=5):
        import feedparser

        url_list=[]
        for i in range(5):
            atom=feedparser.parse('http://b.hatena.ne.jp/'+user_name+'/atomfeed?of='+str(i*20))
            for j in range(len(atom.entries)):
                url_list.append(atom.entries[j]['links'][0]['href'])
        return url_list

    #twitterのタイムラインからurlを取得
    #params access_token_key:twitterのアクセストークン,access_token_secret:twitterのトークンシークレット
    #return urlのリスト
    def userTimelineToUrl(self,access_token_key,access_token_secret):

        import twitter
        import re
        import urllib2
        import time

        consumer_key='Your twitter app consumer key'
        consumer_secret='Your twitter app consumer secret'

        api=twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token_key,access_token_secret=access_token_secret)
        url_list=[]
        pattern='(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;¥\/?:¥@&=+¥$,%#]+)'

        i=0
        while True:
            try:
                time.sllep(1)
                statuses=api.GetUserTimeline(count=200,page=i)
                for s in statuses:
                    match=re.search(pattern,s.text)
                    if match!=None:
                        url_list.append(match.group(0))
                i+=1
                if i==15:
                    break
            except twitter.TwitterError:
                time.sleep(1)
                continue

        return url_list

    #短縮urlを展開
    #params url_list:短縮urlの入ったリスト
    #return 展開されたurlのリスト
    def getRealUrl(self,url_list):

        import gevent
        from gevent import monkey
        monkey.patch_all()

        import urllib2

        def get_url(url,real_url_list):
            try:
                data=urllib2.urlopen(url).geturl()
                real_url_list.append(data)
            except urllib2.HTTPError:
                pass

        real_url_list=[]
        jobs=[gevent.spawn(get_url,url,real_url_list) for url in url_list]
        gevent.joinall(jobs)

        return real_url_list
