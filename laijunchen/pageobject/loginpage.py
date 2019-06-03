# -*- encoding:utf-8 -*-

from laijunchen.utils.webdirver.firefoxdirver import FireFoxDirver
from laijunchen.config import LOGIN_PAGE_URL

class LoginPage():

    def __init__(self):
        self.__dirver = FireFoxDirver().get_dirver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        element = self.__driver.find_element_by_xpath("//*[@class='fs24']")
        return element

    @property
    def input_email_element(self):
        input_email_element = self.__dirver.find_element_by_name('email')
        return input_email_element

    @property
    def input_passwd_element(self):
        input_passwd_element = self.__dirver.find_element_by_name('pwd')
        return input_passwd_element

    @property
    def submit_login_element(self):
        submit_login_element = self.__dirver.find_element_by_id('comm-submit')
        return submit_login_element

    def login(self, name, password):
        self.input_email_element.send_keys(name)
        self.input_passwd_element.send_keys(password)
        self.submit_login_element.click()

    def open_and_check(self):
        '''打开并检测页面是否正确展示，如果正确返回ture，如果不正确返回false'''
        self.__dirver.get(LOGIN_PAGE_URL)

        if self.page_flag.text == u'用户登录':
            return True
        else:
            return False