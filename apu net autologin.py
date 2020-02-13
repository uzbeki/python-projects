from selenium import webdriver
from time import sleep

user_id = '' #university id
password = '' #password

def login():
    driver = webdriver.Chrome("D:\\projects\\webdriver\\chromedriver.exe")
    driver.get("https://webauth.apu.ac.jp/fs/customwebauth/login.html?switch_url=https://webauth.apu.ac.jp/login.html&wlan=APU-Webauth&redirect=webauth.apu.ac.jp/")
    sleep(1)
    username_input = driver.find_element_by_name("username")
    username_input.send_keys(user_id)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)

    login_button = driver.find_element_by_css_selector("body > form > div > table > tbody > tr:nth-child(5) > td > input")
    login_button.click()
    sleep(2)
    driver.quit()

login()
