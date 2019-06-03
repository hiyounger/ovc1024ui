# -*- encoding:utf-8 -*-
from gaolincong.utils.webdriver.firefoxdriver import FirefoxDriver
from gaolincong.config import USERGROU_CREATE_PAGE_URL

class UsergroupCreatePage():
    def __init__(self):
        self.__driver=FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element = self.__driver.find_element_by_xpath("//*[@role='form']/div[3]/label")
        return element

    def open_and_check(self):
        self.__driver.get(USERGROU_CREATE_PAGE_URL)
        if self.page_flag.text == u"小组图标":
            return True
        else:
            return False