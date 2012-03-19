# -*- coding:utf-8 -*-
class socialStream:

    def __init__(self):
        self.consumer_key='your consumer key'
        self.consumer_secret='your consumer secret'

    #facebookのlikeのurlを取得
    #params access_token:facebookのアクセストークン,num:取得したいurlの数
    #return urlのリスト
    def getLikedUrl(self,access_token,num):
        url_list=[]
        try:
            import facebook
            import json

            graph=facebook.GraphAPI(access_token)
            url_like_list=graph.fql("SELECT url FROM url_like WHERE user_id = me() LIMIT "+str(num))
            for url_like_dict in url_like_list:
                url_list.append(url_like_dict["url"])
        except facebook.GraphAPIError:
            import sys
            print sys.exc_info()
        except:
            import sys
            print sys.exc_info()
            
        return url_list
    
    #facebookのshareのurlを取得
    #params access_token:facebookのアクセストークン、num:取得したいurlの数
    #return urlのリスト
    def getSharedUrl(self,access_token,num):
        url_list=[]
        try:
            import facebook
            import json
            
            graph=facebook.GraphAPI(access_token)
                    
            url_share_list=graph.fql("SELECT url FROM link WHERE owner = me() LIMIT "+str(num))
            
            for url_share_dict in url_share_list:
                url_list.append(url_share_dict["url"])
        except facebook.GraphAPIError:
            import sys
            print sys.exc_info()
        except:
            import sys
            print sys.exc_info()

        return url_list
    
    #はてなのidからはてぶしているurlを取得
    #params user_name:はてなid,num:取得したいurlの数
    #return urlのリスト
    def getUrlFromHateb(self,user_name,num=5):
        import feedparser

        url_list=[]
        for i in range(num):
            atom=feedparser.parse('http://b.hatena.ne.jp/'+user_name+'/atomfeed?of='+str(i*20))
            for j in range(len(atom.entries)):
                url_list.append(atom.entries[j]['links'][0]['href'])
        return url_list

    #twitterのタイムラインからurlを取得
    #params access_token_key:twitterのアクセストークン,access_token_secret:twitterのトークンシークレット
    #return urlのリスト
    def userTimelineToUrl(self,access_token_key,access_token_secret,num=15):

        import twitter
        import re
        import urllib2
        import time
        import sys

        # 本番
        consumer_key=self.consumer_key
        consumer_secret=self.consumer_secret

        api=twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token_key,access_token_secret=access_token_secret)
        url_list=[]
        pattern='(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;¥\/?:¥@&=+¥$,%#]+)'

        i=0
        while True:
            print i
            try:
                time.sleep(1)
                statuses=api.GetUserTimeline(count=200,page=i)
                for s in statuses:
                    match=re.search(pattern,s.text)
                    if match!=None:
                        url_list.append(match.group(0))
                i+=1
                if len(url_list)>100:
                    break
                if i==num:
                    break
            except twitter.TwitterError:
                print sys.exc_info()[1][0]
                if sys.exc_info()[1][0]=='This method requires authentication.':
                    #authが切れている場合
                    break
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 150 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 350 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                else:
                    time.sleep(1)
                    continue

        return url_list


    #twitterのretweetからurlを取得
    #params access_token_key:twitterのアクセストークン,access_token_secret:twitterのトークンシークレット
    #return urlのリスト
    def getUserRetweets(self,access_token_key,access_token_secret,num=15):
        print 'getUserRetweets'
        import twitter
        import time
        import sys
        
        consumer_key=self.consumer_key
        consumer_secret=self.consumer_secret
        
        api=twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)
        url_list=[]
        
        max_id=None
        count=100
        i=0

        while True:
            print i
            try:
                statuses=api.GetUserRetweets(count=count,max_id=max_id,include_entities=True)
                for s in statuses:
                    for u in s.urls:
                        if u.expanded_url==None:
                            url_list.append(u.url)
                        else:
                            url_list.append(u.expanded_url)
                    max_id=s.id
                i+=1
                if len(url_list)>200:
                    break
                if i==num:
                    break
            except twitter.TwitterError:
                print "Poko"
                print sys.exc_info()[1][0]
                if sys.exc_info()[1][0]=='This method requires authentication.':
                    # authが切れている場合
                    break
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 150 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 350 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                else:
                    time.sleep(1)
                    continue
        return url_list

    #twitterのfavoriteのurlを取得
    #params access_token:facebookのアクセストークン,num:取得したいurlの数
    #return urlのリスト
    def getFavorites(self,access_token_key,access_token_secret,num=15):
        print 'getFavorites'
        import twitter
        import time
        import sys

        consumer_key=self.consumer_key
        consumer_secret=self.consumer_secret

        api=twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)
        url_list=[]
        i=0
        while True:
            print i
            try:
                statuses=api.GetFavorites(page=i,include_entities=True)
                for s in statuses:
                    for u in s.urls:
                        if u.expanded_url==None:
                            url_list.append(u.url)
                        else:
                            url_list.append(u.expanded_url)
                if len(url_list)>200:
                    break
                i+=1
                if i==num:
                    break
            except twitter.TwitterError:
                print sys.exc_info()[1][0]
                if sys.exc_info()[1][0]=='This method requires authentication.':
                    # authが切れている場合
                    break
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 150 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                elif sys.exc_info()[1][0]=='Rate limit exceeded. Clients may not make more than 350 requests per hour.':
                    # limitに引っかかった場合
                    time.sleep(60*30)
                    continue
                else:
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
            except urllib2.URLError:
                pass
            except:
                pass

        real_url_list=[]

        j=0
        while True:
            try:
                print 'Try',j
                timeout=gevent.Timeout(5*60)
                # timeoutを1分で設定する
                timeout.start()
                jobs=[gevent.spawn(get_url,url,real_url_list) for url in url_list]
                gevent.joinall(jobs)
            except gevent.Timeout:
                print 'Timeout',j
                j+=1
                if j>2:
                    # timeoutしたら、もう一度繰り返す
                    # 3回だめな場合はbreak
                    break
            finally:
                timeout.cancel()
                break

        return real_url_list


    #url->tag_dict
    def getHatebTag(self,url):
        tag_list=[]
        try:
            import urllib
            import json
            
            hateb_base_url='http://b.hatena.ne.jp/entry/jsonlite/?'
            
            query=urllib.urlencode({'url':url})
            hateb_json=urllib.urlopen(hateb_base_url+query).read()

            #記事ごとのタグをまとめるリスト

            if hateb_json!='null':
                hateb_dict=json.loads(hateb_json)
                for hateb_bookmark_dict in hateb_dict['bookmarks']:
                    for t in hateb_bookmark_dict['tags']:
#db保存用
                        t=t.replace('"','')
                        t=t.replace('\n','')
                        t=t.replace('\\','')
                        t=t.replace('*','')
                        t=t.replace('!','')
                        t=t.replace('.','')
                        t=t.replace('@','')
                        t=t.replace('+','')
                        t=t.replace('-','')
                        t=t.replace('\'','')
                        t=t.replace(' ','')
#大文字->小文字
                        t=t.lower()
                        if len(t)!=0:
                            #url一つにつきタグは１個
                            if t not in tag_list:
                                tag_list.append(t)
            
        finally:
            return tag_list


    #url_list->tag_dict
    def getHatebTagFromUrlList(self,url_list):
        tag_dict={}
        for url in url_list:
            for tag in self.getHatebTag(url):
                tag_dict.setdefault(tag,0)
                tag_dict[tag]+=1
        
        return tag_dict


    def deleteUselessUrl(self,url_list):
        import re

        real_url_list=[]

        regular_list=[re.compile('http://ustre\.am'),re.compile('http://http://tweetphoto\.com')]
        for url in url_list:
            for regular in regular_list:
                if regular.match:
                    real_url_list.append(url)

        return real_url_list
