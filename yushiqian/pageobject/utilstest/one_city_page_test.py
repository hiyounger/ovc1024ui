# -*-encoding:utf-8-*-
import unittest
from yushiqian.pageobject.utils.userutils import UserUtils
from yushiqian.pageobject.one_city_page import OneCityPage
from yushiqian.pageobject.loginpage import LoginPage
import time
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        username = '763208734@qq.com'
        password = 'yu75321ysq'
        LoginPage().open_and_check()
        UserUtils().login(username, password)
        time.sleep(5)

    def test_open_user_group_page(self):

        self.assertTrue(OneCityPage().open_and_check())



if __name__ == '__main__':
    unittest.main()
