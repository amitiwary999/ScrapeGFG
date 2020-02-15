from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
import sys
try:
    flag="idlelib" in sys.modules
#   name=input("enter the company name like Amazon\n")
    article_links="https://www.artistize.com/Explore/people?order=2&page="
    path=((r'/home/meera/Desktop/Artistize_detail'))
    if not os.path.exists(path):
        os.makedirs(path)
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    fob=open(os.path.join(path,'artist1.txt'),'w')
    for loop in range(1884, 3529):
        detail = ""
        article_links = "https://www.artistize.com/Explore/people?order=2&page="+str(loop)
        r = requests.get(article_links, headers=headers, timeout=5)
        paged = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('div',{'class':'ExBlock2'}))

        for nag in paged.find_all('div',{'class':'row wrapper-row one'}):
            for fir in nag.find_all('div',{'class':'col-lg-6 col-xs-12 People_height no-padding'}):
                detail = detail+"\n"
                #detail = detail.rstrip()
                for names in fir.find_all('h3',{'class':'titlecaption'}):
                    for name in names.find_all("a"):
                        #print(name.text)
                        newStr = name.text.split()
                        cor = ' '.join(newStr)
                        detail = detail+cor
                        detail.strip()
                        #detail = detail.rstrip()
                        
                for sec in fir.find_all('div', {'class': 'exp-obj-desc-wrapper'}):
                    for paragraph in sec.find_all(["p"]):
                        #print(paragraph.text)
                        newStr = paragraph.text.split()
                        cor = ' '.join(newStr)  
                        detail = detail+"\t"+cor
                        detail.strip()
                        #detail = detail.rstrip()
     
        #print(detail)
        for nag in paged.find_all('div',{'class':'row wrapper-row '}):
            for fir in nag.find_all('div',{'class':'col-lg-6 col-xs-12 People_height no-padding'}):
                detail = detail+"\n"
                for names in fir.find_all('h3',{'class':'titlecaption'}):
                    for name in names.find_all("a"):
                        #print(name.text)
                        newStr = name.text.split()
                        cor = ' '.join(newStr)
                        detail = detail+cor
                        detail.strip()
                        #detail = detail.rstrip()
                for sec in fir.find_all('div', {'class': 'exp-obj-desc-wrapper'}):
                    for paragraph in sec.find_all(["p"]):
                        #print(paragraph.text)
                        newStr = paragraph.text.split()
                        cor = ' '.join(newStr)  
                        detail = detail+"\t"+cor
                        detail.strip()
                        #detail = detail.rstrip()

                #newStr = detail.split()
                #cor = ' '.join(newStr)
                #print(cor)
        fob.write(detail)                
    #print(detail)                           
    #fob.write(detail)
    fob.close()
        
#    page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('section'))
#    links=[]
#    for pagen in page.find_all('nav',{'id':'nav-below'}):
#        
#        for pageno in pagen.find_all('a',{'class':'last'}):
#            no=pageno.get("href")
#            number=int(no[-3:-1])
#            print(number)
#        for loop in range(1,number+1):
#            if(loop!=1):
#                article_links="http://www.geeksforgeeks.org/tag/"+name+"/page/"+str(loop)+"/"
#                r=requests.get(article_links, headers=headers)
#                page=BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('section'))
#            for title in page.find_all('h2',{'class':'entry-title'}):
#                for txt in title.find_all("a"):
#                    #print(txt.get("href"))
#                    links.append(txt.get("href"))
#
#            for link in links:
#                title=" "
#                article_detail=[]
#                article=" "
#                r = requests.get(link, headers=headers)    
#                page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('article'))
#                for header in page.find_all('header',{'class':'entry-header'}):
#                    for titl in header.find_all('h1',{'class':'entry-title'}):
#                        title=titl.text
#                #print(path+title+' .txt')
#                article_detail.append(title)
#                fob=open(os.path.join(path,title+'.txt'),'w')        
#                for article in page.find_all('div',{'class':'entry-content'}):
#                    for paragraph in page.find_all(["p","ol","ul"]):
#                         if(sys.version_info >= (3, 0)):
#                             article_detail.append(paragraph.text.translate(non_bmp_map))
#                             article= "\n".join(article_detail)
#                     
#                         else:
#                             reload(sys)
#                             sys.setdefaultencoding('utf-8')
#                             article_detail.append(paragraph.text)
#                             article= "\n".join(article_detail)
                #print(article+"\n\n\n")        
#                fob.write(article)
#                fob.close()
except requests.RequestException as e :
    print(str(e))
    print("error")
