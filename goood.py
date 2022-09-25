from nturl2path import url2pathname
from spider import SpiderHTML
from tqdm import tqdm
import sys
init_url='https://www.gooood.cn/category/type/architecture'
store_path='gooood'

def is_Chinese_p(p):
    for ch in p.contents:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

#def is_Chinese_sentence(sentence):


def has_childtag(tag):
    return  tag.findChidren()==[]

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
        
    def len_object(self,href):
        return len(href)

    def collectData(self,hrefs):
        text_list=[]
        src_list=[]
        for i in tqdm(range(len(hrefs)),desc="collectData"):
            
            image_src=[]
            url= "https://www.gooood.cn/"+str(hrefs[i])
            content=self.getUrl(url)
            p_list=content.find_all('p')
            filter(has_childtag,p_list)
            filter(is_Chinese_p,p_list)
            
            img_list=content.find_all("img")
            for img in img_list:
                image_src.append(img.attrs['src'])
            text_list.append(p_list)
            img_list.append(image_src)
        return text_list,img_list





    

if __name__=='__main__':
    pageEnd=sys.argv[1]
    spider=gooodCollectionSpider(init_url,pageEnd)
    hrefs=spider.collectLink()
    spider.collectData(hrefs)
    

