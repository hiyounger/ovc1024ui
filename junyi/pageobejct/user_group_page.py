# -*- encoding:utf-8 -*-
from junyi.pageobejct.basepage import BasePage
from junyi.config import USEGROUP_PAGE_URL


class UserGroupPage(BasePage):

    url = USEGROUP_PAGE_URL
    page_flag_xpath = "//nav[@class='position-relative']/a"
    page_flag_keyword = u"创建小组"
