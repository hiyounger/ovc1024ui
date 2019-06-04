# -*- encoding:utf-8 -*-
from gaolincong.pageobject.basepage import Basepage
from gaolincong.config import USER_TONGCHENG_PAGE_URL

class UserTongChengPage(Basepage):
    url=USER_TONGCHENG_PAGE_URL
    xpath="//*[@class='card-header']"
    keyword=u"选择加入同城"