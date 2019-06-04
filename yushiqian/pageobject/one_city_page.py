# -*- encoding:utf-8 -*-
from base_page import BasePage
from yushiqian.config import ONECITY_URL

class OneCityPage(BasePage):
    page_url = ONECITY_URL
    page_flag_xpath = "//div[@class='card-header']"
    page_flag_keyword = u'选择加入同城'

