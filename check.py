from bs4 import BeautifulSoup, SoupStrainer
from gtts import gTTS
import requests
import os
import sys
try:
    article_links=input("enter\n")
    path="/home/amit/Desktop/"
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
        print(path+title+' .txt')
        article_detail.append(title)
        fob=open(path+title+' .txt','w')        
        for article in page.find_all('div',{'class':'entry-content'}):
            for paragraph in page.find_all(["p","ol"]):
                article_detail.append(paragraph.text.translate(non_bmp_map))
                article= "\n".join(article_detail)
        print(article+"\n\n\n")        
        fob.write(article)
        fob.close()
except requests.RequestException as e :
    print(str(e))
    print("error")
