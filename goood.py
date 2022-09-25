from nturl2path import url2pathname
from spider import SpiderHTML
from tqdm import tqdm
import sys
init_url='https://www.gooood.cn/category/type/architecture'
store_path='gooood'

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

class gooodCollectionSpider(SpiderHTML):
    def __init__(self,init_url,pageEnd):
        self.init_url=init_url
        self.pageEnd=pageEnd

        
    def collectLink(self):
        hrefs=[]
        for i in tqdm(range(1,self.pageEnd),desc='collectLink'):
            page_url=self.init_url+'/{}'.format(i)
            content=self.getUrl(page_url)
            a_list=content.find_all('a',class_='cover-link',href=True)
            for a in a_list:
                hrefs.append(a.attrs['href'])

            #hrefs.append(href)
            return hrefs
    
    def collectData(self,hrefs):
        for i in tqdm(range(len(hrefs)),desc="collectData"):
            url= "https://www.gooood.cn/"+str(hrefs[i])
            

    

if __name__=='__main__':
    pageEnd=sys.argv[1]
    spider=gooodCollectionSpider(init_url,pageEnd)
    hrefs=spider.collectLink()
    spider.collectData(hrefs)
    
