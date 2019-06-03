# -*- encoding:utf-8 -*-

from junyi.utils.webdriver.firefoxdriver import FirefoxDriver
from junyi.config import LOGIN_PAGE_URL

class UserUtils():

    @classmethod
    def login(cls, email, password):
        __driver = FirefoxDriver().get_driver()
        __driver.get(LOGIN_PAGE_URL)

        input_email_elemnet = __driver.find_element_by_name('email')
        input_email_elemnet.send_keys(email)

        input_passwd_element = __driver.find_element_by_name('pwd')
        input_passwd_element.send_keys(password)

        submit_login_element = __driver.find_element_by_id('comm-submit')
        submit_login_element.click()


