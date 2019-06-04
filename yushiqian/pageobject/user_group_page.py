# -*- encoding:utf-8 -*-
from base_page import BasePage
from yushiqian.config import USERGROUP_URL

class UserGroupPage(BasePage):
    page_url = USERGROUP_URL
    page_flag_xpath = "//nav[@class='position-relative']/a"
    page_flag_keyword = u"创建小组"

