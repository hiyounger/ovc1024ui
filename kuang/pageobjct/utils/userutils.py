#  encoding:utf-8

from kuang.utils.webdriver.firefoxdriver import FirefoxDriver
from kuang.config import LOGIN_PATH_URL


class UserUtils():
    @classmethod
    def login(cls,email,password):
        __driver = FirefoxDriver().get_driver()
        __driver.get(LOGIN_PATH_URL)


        input_email_element = __driver.find_element_by_name('email')
        input_email_element.send_keys(email)


        input_passwd_element =__driver.find_element_by_name('pwd')
        input_passwd_element.send_keys(password)

        submit_login_element=__driver.find_element_by_id('comm-submit')
        submit_login_element.click()