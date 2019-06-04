# -*-encoding:utf-8-*-
import unittest
from gaolincong.pageobject.utils.userutils import UserUtils
from gaolincong.pageobject.user_group_page import UserGroupPage
from gaolincong.pageobject.usergroup_create_page import UsergroupCreatePage
from gaolincong.pageobject.user_tongcheng_page import UserTongChengPage
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        username = '1690344964@qq.com'
        password = '6149762364'
        UserUtils().Login(username,password)
        time.sleep(5)
    def test_something(self):
        UserGroupPage().open_and_check()
    def test_usergroup_create_page(self):
        result=UsergroupCreatePage().open_and_check()
        self.assertTrue(result)
    def test_usertongchengpage(self):
        result=UserTongChengPage().open_and_check()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
