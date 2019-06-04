# encoding:utf-8
from WZ_603.utils.webdeiver.firefoxdriver import FirefoxDriver
from WZ_603.config import USER_PAGE_URL

class UserGroupPage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        element = self.__driver.find_element_by_link_text("创建小组")
        return element
    def open_and_check(self):
        self.__driver.get(USER_PAGE_URL)

        if self.page_flag.text == "创建小组":
            return True
        else:
            return False
