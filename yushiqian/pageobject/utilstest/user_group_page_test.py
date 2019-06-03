import unittest
from yushiqian.pageobject.utils.userutils import UserUtils
from yushiqian.pageobject.user_group_page import UserGroupPage
from yushiqian.pageobject.loginpage import LoginPage
import time


class TestUserGroupPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        username = '763208734@qq.com'
        password = 'yu75321ysq'
        LoginPage().open_and_check()
        UserUtils().login(username, password)
        time.sleep(5)

    def test_open_user_group_page(self):

        UserGroupPage().open_and_check()






if __name__ == '__main__':
    unittest.main()
