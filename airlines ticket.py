import selenium
from selenium import common
from bs4 import BeautifulSoup
import urllib.request
import requests
dan = "Oita"
gacha = " Tokyo (Narita) - NRT"
driver = selenium.webdriver.Chrome("D:\\projects\\webdriver\\chromedriver.exe")
jetstar_url = "https://www.jetstar.com/jp/en/home"
selected_dates_link = "https://www.jetstar.com/jp/en/home?adults=2&children=0&destination=NRT&flexible=1&flight-type=2&infants=0&origin=OIT&selected-departure-date=16-02-2020&selected-return-date=20-02-2020&tab=1"
session_id = ""

driver.get(jetstar_url)


#driver.get(selected_dates_link)
destination = driver.find_element_by_id("search-inbound-xhg7s_iKe")
destination.send_keys(gacha)

