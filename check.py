from bs4 import BeautifulSoup, SoupStrainer
from gtts import gTTS
import requests
import os
import sys
try:
    article_links=input("enter\n")
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
 
    r = requests.get(article_links, headers=headers, timeout=5)
        
    page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('section'))
    for title in page.find_all('h2',{'class':'entry-title'}):
        for txt in title.find_all("a"):
            #print(txt.text)
            print(txt.get("href"))
except requests.RequestException as e :
    print(str(e))
    print("error")
