# -*- encoding:utf-8 -*-
from laijunchen.pageobject.test.basepage import BasePag
from laijunchen.config import USER_GROUP_PAGE


class UserGroupCreatePage(BasePag):

    url = USER_GROUP_PAGE
    page_flag_xpath = "//form[@role='form']/div[2]/label"
    page_flag_keyword = u"小组介绍"

