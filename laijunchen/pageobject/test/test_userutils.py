# -*- encoding:utf-8 -*-
import unittest
from laijunchen.pageobject.utils.userutils import UserUtils

class TestUserUtils(unittest.TestCase):
    def test_userlogin(self):
        username = '382135230@qq.com'
        password = "Ljc960614"
        UserUtils.login(username, password)


if __name__ == '__main__':
    unittest.main()
