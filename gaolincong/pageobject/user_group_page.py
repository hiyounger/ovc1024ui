# -*- encoding:utf-8 -*-
from gaolincong.pageobject.basepage import Basepage
from gaolincong.config import USEGROUP_PAGE_URL

class UserGroupPage(Basepage):
    url = USEGROUP_PAGE_URL
    xpath = "//*[@class='btn btn-sm btn-info position-absolute']"
    keyword = u"创建小组"
