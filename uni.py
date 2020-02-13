import requests
from bs4 import BeautifulSoup

url = "https://cwur.org/2019-2020.php"
r= requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"})
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', class_='table')
tbody = table.find('tbody')

top = eval(input("TOP how many universities do you wish to see: "))
print()
print("Top " + str(top) + " world university rankings (CWUR)")


for i in tbody.find_all('tr'):
    rank = int(i.find_all('td')[0].text.strip())
    name = i.find_all('td')[1].a.text.strip()
    score = float(i.find_all('td')[8].text.strip())
    if rank<=top:
        print(rank, name, score)
    
