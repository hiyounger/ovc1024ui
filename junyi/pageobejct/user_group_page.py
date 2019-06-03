# -*- encoding:utf-8 -*-
from junyi.utils.webdriver.firefoxdriver import FirefoxDriver
from junyi.config import USEGROUP_PAGE_URL

class UserGroupPage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        # element = self.__driver.find_element_by_link_text("创建小组")
        # return element
        return self.create_group_button

    @property
    def create_group_button(self):
        element = self.__driver.find_element_by_link_text("创建小组")
        return element

    def open_and_check(self):
        '''打开并检测页面是否正确展示，如果正确返回true，如果不正确返回false'''
        self.__driver.get(USEGROUP_PAGE_URL)

        if self.page_flag.text == u"创建小组":
            return True
        else:
            return False




