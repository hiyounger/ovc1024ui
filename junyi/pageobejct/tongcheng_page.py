# -*- encoding:utf-8 -*-

from junyi.pageobejct.basepage import BasePage
from junyi.config import TONGCHENG_PAGE_URL


class TongChengPage(BasePage):

    url = TONGCHENG_PAGE_URL
    page_flag_xpath = "//div[@class='card-header']"
    page_flag_keyword = u"选择加入同城"

