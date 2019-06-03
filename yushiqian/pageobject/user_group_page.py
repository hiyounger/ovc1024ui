# -*- encoding:utf-8 -*-
from yushiqian.pageobject.webdriver.firefoxdriver import FirefoxDriver
from yushiqian.config import USERGROUP
from yushiqian.utils.log import debug


class UserGroupPage():
    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        # element = self.__driver.find_element_by_link_text("创建小组")
        # return element
        debug('获取 元素标签')
        return self.create_group_button()

    def create_group_button(self):
        element = self.__driver.find_element_by_link_text("创建小组")
        debug('获取 创建小组 元素')
        return element

    def open_and_check(self):
        self.__driver.get(USERGROUP)
        if self.page_flag.text == u'创建小组':
            return True
        else:
            return False
