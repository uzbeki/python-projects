import requests
from bs4 import BeautifulSoup

def latest_news_kun():
        url = 'http://kun.uz'
        sp = BeautifulSoup(requests.get(url).text, 'html.parser')
        links=sp.findAll('a', class_='daily-block js-day-line-item')
        #print(type(links))
        print("Kun.uz dagi eng so'nggi yangiliklar:")
        print()
        for i in links:
                print(i.text)
                newslink= 'http://kun.uz' + str(i['href'])
                print(newslink)
                print()

        #yangiliklarni nomini olish
        #ntitle=sp.findAll('p', class_='news-title')
        #	print(ntitle[0]) #faqat newsni titleni oliw
        #for i in ntitle:
        #		print(i.text)
        #		print()
        if input("programma yopilsinmi?: ") == "yes":
                quit()



latest_news_kun()
