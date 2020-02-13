import requests #saytga kirish uchun
from bs4 import BeautifulSoup #sayt malumotlarini olish uchun
import urllib.request #fayllarni yuklaw un

url = "http://yoshlar.com"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

print("Yoshlar.com sayti sizni qo'lingizda. Nima xohlaysiz? Bulardan birini tanlang" )

# give option to choose among
# "uzmuzik", "russkie", "euro", "clips", "konsert", "kino"
print("uzmusic, russkie, euro, clips, konsert, kino")
# get the input
tanlov = ["uzmusic", "russkie", "euro"]#, "clips", "konsert", "kino"]
istak = input("berilganday xatosiz yozing: ")
#output the necessary content(div id=allEntries > a) to choose from
wanted_page = "http://yoshlar.com/" + str(istak)
new_soup = BeautifulSoup(requests.get(wanted_page).content, "html.parser")
title = new_soup.find("title").text.split("-")[0]
fayllar = new_soup.find(id="allEntries").select("a")[::2]
 
def yukla():
    yuklaw_soni = 1
    fayllar_soni = len(fayllar)
    for i in fayllar: # agar allentriesdagi a larda 
        file_url = "http://yoshlar.com/" + str(i['href']) #yangi url tuz
        file_soup = BeautifulSoup(requests.get(file_url).content, "html.parser") #bs4ga tawa uwani ochish uchun
        file_a = file_soup.select(".download2") #
        for i in file_a:
            file_link = url + i.get('href')
            file_name = i.get('download')
            print(str(yuklaw_soni)+ "/" + str(fayllar_soni) + "-chi fayl")
            print(file_name, " yuklanyapti...")
            yuklaw_soni += 1
            #urllib.request.urlretrieve(file_link, file_name)
            
             
    

def sura():
    print(title)
    print("sahifadagi hammasini yuklab olasizmi? ha/yoq")
    javob = input("berilganday javob yozing: ")
    if javob == "ha":
        yukla()
    else:
        print("sog' bo'ling unda")


sura()
