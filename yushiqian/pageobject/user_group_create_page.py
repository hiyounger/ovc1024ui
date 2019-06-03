# -*- encoding:utf-8 -*-
from yushiqian.pageobject.webdriver.firefoxdriver import FirefoxDriver
from yushiqian.config import USEGROUP_PAGE_URL
import time

class UserGroupCreatePage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        element = self.__driver.find_element_by_xpath("//form[@role='form']/div[2]/label")
        return element
        # return self.create_group_button

    def check_if_page_open(self):
        time.sleep(5)
        if self.page_flag.text == u"小组介绍":
            return True
        else:
            return False
