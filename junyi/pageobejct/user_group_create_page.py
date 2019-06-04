# -*- encoding:utf-8 -*-
from junyi.pageobejct.basepage import BasePage
from junyi.config import USEGROUP_PAGE_URL

class UserGroupCreatePage(BasePage):

    url = USEGROUP_PAGE_URL
    page_flag_xpath = "//form[@role='form']/div[2]/label"
    page_flag_keyword = u"小组介绍"

