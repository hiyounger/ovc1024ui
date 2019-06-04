# -*- encoding:utf-8 -*-
from base_page import BasePage
from yushiqian.config import USEGROUP_PAGE_URL

class UserGroupCreatePage(BasePage):
    page_url = USEGROUP_PAGE_URL
    page_flag_xpath = "//form[@role='form']/div[2]/label"
    page_flag_keyword = u"小组介绍"

