# -*- encoding:utf-8 -*-
from gaolincong.utils.webdriver.firefoxdriver import FirefoxDriver
from gaolincong.config import LOGIN_PAGE_URL

class Login():
    def __init__(self):
        self.__driver=FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element=self.__driver.find_element_by_class_name('fs24')
        return element
    @property
    def input_email(self):
        input_email = self.__driver.find_element_by_name('email')
        return input_email
    @property
    def input_pwd(self):
        input_pwd = self.__driver.find_element_by_name('pwd')
        return input_pwd
    @property
    def login_button(self):
        login_button = self.__driver.find_element_by_id('comm-submit')
        return login_button
    def login(self,email,pwd):
        self.input_email.send_keys(email)
        self.input_pwd.send_keys(pwd)
        self.login_button.click()
    def open_and_check(self):
        self.__driver.get(LOGIN_PAGE_URL)
        if self.page_flag.text==u"用户登录":
            return True
        else:
            return False
