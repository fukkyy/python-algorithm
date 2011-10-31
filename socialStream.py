# -*- coding:utf-8 -*-

class socialStream:

    def getLikeToUrl(access_token,num):
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

    def getHatebFromUser(user_name,num=5):
        import feedparser

        url_list=[]
        for i in range(5):
            atom=feedparser.parse('http://b.hatena.ne.jp/'+user_name+'/atomfeed?of='+str(i*20))
            for j in range(len(atom.entries)):
                url_list.append(atom.entries[j]['links'][0]['href'])
        return url_list

    def userTimelineToUrl(self,consumer_key,consumer_secret,access_token_key,access_token_secret):

        import twitter
        import re
        import urllib2
        import time

        api=twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token_key,access_token_secret=access_token_secret)
        url_list=[]
        pattern='(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;¥\/?:¥@&=+¥$,%#]+)'

        i=0
        while True:
            try:
                time.sllep(1)
                statuses=api.GetUserTimeline(screen_name='fukkyy',count=200,page=i)
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
