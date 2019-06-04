# -*- encoding:utf-8 -*-
from gaolincong.pageobject.basepage import Basepage
from gaolincong.config import USERGROU_CREATE_PAGE_URL

class UsergroupCreatePage(Basepage):
    url = USERGROU_CREATE_PAGE_URL
    xpath = "//*[@role='form']/div[3]/label"
    keyword = u"小组图标"