# -*- encoding:utf-8 -*-
import unittest
from laijunchen.pageobject.utils.userutils import UserUtils
from laijunchen.pageobject.tongcheng_page import TongChengPage
import time

class TestTongChen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        username = '382135230@qq.com'
        password = "Ljc960614"
        UserUtils.login(username, password)
        time.sleep(5)

    def test_open_user_group_page(self):
        self.assertTrue(TongChengPage().open_and_check())

if __name__ == '__main__':
    unittest.main()
