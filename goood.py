from nturl2path import url2pathname
from spider import SpiderHTML
from tqdm import tqdm
import sys
init_url='https://www.gooood.cn/category/type/architecture'
store_path='gooood'

class gooodCollectionSpider(SpiderHTML):
    def __init__(self,init_url,pageEnd):
        self.init_url=init_url
        self.pageEnd=pageEnd

        
    def collectLink(self):
        hrefs=[]
        for i in tqdm(range(1,923)):
            page_url=self.init_url+'/{}'.format(i)
            content=self.getUrl(page_url)
            href=content.find_all('a',class_='cover-link',href=True).attrs['href']
            hrefs.append(href)
            return hrefs

if __name__=='__main__':
    pageEnd=sys.argv[1]
    spider=gooodCollectionSpider(init_url,pageEnd)
    print(spider.collectLink())
