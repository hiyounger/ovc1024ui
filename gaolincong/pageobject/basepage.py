# -*- encoding:utf-8 -*-
from gaolincong.utils.webdriver.firefoxdriver import FirefoxDriver

class Basepage():
    url=None
    xpath=None
    keyword=None

    def __init__(self):
        self.__driver=FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element = self.__driver.find_element_by_xpath(self.xpath)
        return element

    def open_and_check(self):
        self.__driver.get(self.url)
        if self.page_flag.text == self.keyword:
            return True
        else:
            return False