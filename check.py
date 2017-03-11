from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
import sys
try:
    flag="idlelib" in sys.modules
    name=input("enter the company name like Amazon\n")
    article_links="http://www.geeksforgeeks.org/tag/"+name+"/"
    path=((r'/home/amit/Desktop/Interview_%s')% (name))
    if not os.path.exists(path):
        os.makedirs(path)
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
 
    r = requests.get(article_links, headers=headers, timeout=5)    
    page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('section'))
    links=[]
    for title in page.find_all('h2',{'class':'entry-title'}):
        for txt in title.find_all("a"):
            #print(txt.get("href"))
            links.append(txt.get("href"))

    for link in links:
        title=" "
        article_detail=[]
        article=" "
        r = requests.get(link, headers=headers, timeout=5)    
        page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('article'))
        for header in page.find_all('header',{'class':'entry-header'}):
            for titl in header.find_all('h1',{'class':'entry-title'}):
                title=titl.text
        #print(path+title+' .txt')
        article_detail.append(title)
        fob=open(os.path.join(path,title+' .txt'),'w')        
        for article in page.find_all('div',{'class':'entry-content'}):
            for paragraph in page.find_all(["p","ol","ul"]):
                 if(sys.version_info >= (3, 0)):
                     article_detail.append(paragraph.text.translate(non_bmp_map))
                     article= "\n".join(article_detail)
                     
                 else:
                     reload(sys)
                     sys.setdefaultencoding('utf-8')
                     article_detail.append(paragraph.text)
                     article= "\n".join(article_detail)
        #print(article+"\n\n\n")        
        fob.write(article)
        fob.close()
except requests.RequestException as e :
    print(str(e))
    print("error")
