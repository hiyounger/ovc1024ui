# -*- encoding:utf-8 -*-
from base_page import BasePage
from yushiqian.config import LOGIN_URL


class LoginPage(BasePage):
    page_url = LOGIN_URL
    page_flag_xpath = "//div[@class='card-body']/div"
    page_flag_keyword = u"用户登陆"


    @property
    def input_email_element(self):
        input_email_element = self.driver.find_element_by_name('email')
        return input_email_element

    @property
    def input_passwd_element(self):
        input_passwd_element = self.driver.find_element_by_name('pwd')
        return input_passwd_element

    @property
    def submit_login_element(self):
        submit_login_element = self.driver.find_element_by_id('comm-submit')
        return submit_login_element

    def login(self, email, password):
        self.input_email_element.send_keys(email)
        self.input_passwd_element.send_keys(password)
        self.submit_login_element.click()
