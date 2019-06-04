# -*- encoding:utf-8 -*-
from yushiqian.pageobject.webdriver.firefoxdriver import FirefoxDriver
from yushiqian.config import ONECITY_URL
from yushiqian.utils.log import debug


class OneCityPage():
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
        element = self.__driver.find_element_by_xpath("//div[@class='card-header']")
        debug('获取 选择加入同城 元素')
        return element

    def open_and_check(self):
        self.__driver.get(ONECITY_URL)
        if self.page_flag.text == u'选择加入同城':
            return True
        else:
            return False