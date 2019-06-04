# -*- encoding:utf-8 -*-
from junyi.utils.webdriver.firefoxdriver import FirefoxDriver
import time


class BasePage():

    url = None
    page_flag_xpath = None
    page_flag_keyword = None

    def __init__(self):
        self.driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        '''定义页面识别元素'''
        element = self.driver.find_element_by_xpath(self.page_flag_xpath)
        return element
        # return self.create_group_button

    def open_and_check(self):
        self.driver.get(self.url)
        return self.check_if_page_open()

    def check_if_page_open(self):
        time.sleep(5)
        if self.page_flag.text == self.page_check_keyword:
            return True
        else:
            return False

