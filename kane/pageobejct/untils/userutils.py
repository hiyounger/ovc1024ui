# -*- encoding:utf-8 -*-

from  kane.untils.webdriver.firefosdriver import FirefoxDriver
from kane.config import LOGIN_PAGE_URL

class UserUtils():

    @classmethod
    def login(cls,email,password):
        __driver = FirefoxDriver().get_driver()
        __driver.get(LOGIN_PAGE_URL)

        input_email_element = __driver.find_element_by_name('email')
        input_email_element.send_keys(email)

        input_password_element = __driver.find_element_by_name('pwd')
        input_password_element.send_keys(password)

        submit_login_element = __driver.find_element_by_id('comm-submit')
        submit_login_element.click()