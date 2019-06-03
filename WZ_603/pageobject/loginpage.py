# -*- encoding:utf-8 -*-

from  WZ_603.utils.webdeiver.firefoxdriver import FirefoxDriver
from WZ_603.config import LOGIN_PAGE_URL

class LoginPage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element = self.__driver.find_element_by_xpath("//*[@class='fs24']")
        return element
    @property
    def input_email_element(self):
        input_email_element = self.__driver.find_element_by_name('email')
        return input_email_element
    @property
    def input_passwd_element(self):
        input_passwd_element = self.__driver.find_element_by_name("pwd")
        return input_passwd_element
    @property
    def submit_login_element(self):
        submit_login_element = self.__driver.find_element_by_id("'comm-submit'")
        return submit_login_element
    def login(self,email,password):
        self.input_email_element.send_keys(email)
        self.input_passwd_element.send_keys(password)
        self.submit_login_element.click()

    def open_and_check(self):
        self.__driver.get(LOGIN_PAGE_URL)
        if self.page_flag.text == "用户登录":
            return True
        else:
            return False