# -*- encoding:utf-8 -*-
from gaolincong.utils.webdriver.firefoxdriver import FirefoxDriver
from gaolincong.config import USEGROUP_PAGE_URL

class UserGroupPage():
    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element = self.__driver.find_element_by_xpath("//*[@class='btn btn-sm btn-info position-absolute']")
        return element
    def open_and_check(self):
        self.__driver.get(USEGROUP_PAGE_URL)
        if self.page_flag.text==u"创建小组":
            return True
        else:
            return False