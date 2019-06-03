# -*- encoding:utf-8 -*-
import unittest
from laijunchen.pageobject.utils.userutils import UserUtils
from laijunchen.pageobject.user_group_page import UsergroupPage
import time

class TestUserGroupPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        username = '382135230@qq.com'
        password = "Ljc960614"
        UserUtils.login(username, password)
        time.sleep(5)

    def test_open_user_group_page(self):
        UsergroupPage().open_and_check()



if __name__ == '__main__':
    unittest.main()
