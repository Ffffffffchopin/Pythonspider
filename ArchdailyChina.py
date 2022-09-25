# -*_ coding:utf-8 -*_

from spider import SpiderHTML
import sys,os,re
import requests
__author__='fffchopin'

#主页
homepageurl='https://www.archdaily.cn/search/cn/projects?page=2'
#存储文件夹
store_path='./ArchdailyChina'

class ArchdailyChinaSpider(SpiderHTML):
    def __init__(self,count,url):
        self.url=url
        self.count=count

    def start(self):
        #url=self.url+''
        r = requests.get(self.url)
        print(r.cookies)
        #content=self.getUrl(self.url)
        #print (content.)      




if __name__=='__main__':
    count=sys.argv[1]
    spider=ArchdailyChinaSpider(count,homepageurl)
    spider.start()
