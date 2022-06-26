from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class YaLogin():
    
    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.filename = 'task3-ya-selenium/login.txt'
        
    
    def _get_login_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            self.data = f.read().split()
        return self.data
        
    def ya_login(self):
        self.browser.get('https://passport.yandex.ru/auth')
        self.browser.find_element_by_xpath(
            '//input[@data-t="field:input-login"]'
            ).send_keys(self._get_login_data(self.filename)[0])
        self.browser.find_element_by_xpath(
            '//button[@data-t="button:action:passp:sign-in"]'
            ).click()
        self.browser.implicitly_wait(2)
        self.browser.find_element_by_xpath(
            '//input[@data-t="field:input-passwd"]'
            ).send_keys(self._get_login_data(self.filename)[1])
        self.browser.find_element_by_xpath(
            '//button[@data-t="button:action:passp:sign-in"]'
            ).click()  

if __name__ == '__main__':
    
    tester = YaLogin()
    tester.ya_login()
