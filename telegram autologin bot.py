from selenium import webdriver
from time import sleep

class Telegrambot():
    def __init__(self):
        self.driver = webdriver.Chrome('D:\\projects\\webdriver\\chromedriver.exe')

    def login(self):
        print('accessing the web...')
        self.driver.get("https://web.telegram.org/#/login")
        sleep(2)
       
        code = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input')
        code.clear()
        code.send_keys('+81') #area code

        phone = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
        phone.send_keys('') #enter your phone number

        next_btn = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a')
        next_btn.click()
        sleep(1)

        ok_btn = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]/span')
        ok_btn.click()
        sleep(1)

        code = input("what is the code sent to your telegram account: ")
        sleep(0.8)
        code_in = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[4]/input')
        sleep(1)
        code_in.send_keys(code)
        sleep(1.5)

        pass_in = self.driver.find_element_by_css_selector('body > div.page_wrap > div > div.login_page > div.login_form_wrap > form > div.md-input-group.md-input-animated > input')
        pass_in.send_keys('') #enter two step verification key

        next2 = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a/my-i18n')
        next2.click()
        sleep(2)
        
        nimdumbul = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li[2]/a/div[3]/div[1]')
        sleep(0.3)
        nimdumbul.click()

        typer = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')
        message = input("message to send: ")
        typer.send_keys(message)

        send = self.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[3]/button/span[1]')
        send.click()



Tbot = Telegrambot()
Tbot.login()
