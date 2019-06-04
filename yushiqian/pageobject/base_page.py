# -*- encoding:utf-8 -*-
from yushiqian.pageobject.webdriver.firefoxdriver import FirefoxDriver


class BasePage():
    page_url = None
    page_flag_xpath = None
    page_flag_keyword = None

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        element = self.__driver.find_element_by_xpath(self.page_flag_xpath)
        # debug('获取 元素标签')
        return element

    def open_and_check(self):
        self.__driver.get(self.page_url)
        if self.page_flag.text == self.page_flag_keyword:
            return True
        else:
            return False
