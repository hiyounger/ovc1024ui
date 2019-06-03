# -*- encoding:utf-8 -*-
from kane.untils.webdriver.firefosdriver import FirefoxDriver
from kane.config import USEGROUP_PAGE_URL

class UserGruopPage():

    def __init__(self):
        self.__driver = FirefoxDriver().get_driver()

    @property
    def page_flag(self):
        # element = self.__driver.find_element_by_link_text("创建小组")
        return self.create_group_button

    @property
    def create_group_button(self):
        element = self.__driver.find_element_by_link_text("创建小组")
        return element

    def open_and_check(self):

        self.__driver.get(USEGROUP_PAGE_URL)

        if self.page_flag.text == u"创建小组":
            return True
        else:
            return False