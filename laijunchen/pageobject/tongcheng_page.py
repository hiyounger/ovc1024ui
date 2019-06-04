# -*- encoding:utf-8 -*-
from laijunchen.pageobject.test.basepage import BasePag
from laijunchen.config import TONGCHENG_PAGE_URL


class TongChengPage(BasePag):

    url = TONGCHENG_PAGE_URL
    page_flag_xpath = "//div[@class='card-header']"
    page_flag_keyword =u"选择加入同城"

