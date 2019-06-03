# encoding:utf-8
import unittest
from WZ_603.pageobject.user_group_page import UserGroupPage
from WZ_603.pageobject.utils.userutil import UserUtills
import time

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        usernamen = "896417651@qq.com"
        password = "w896417651"
        UserUtills.login(usernamen,password)
        time.sleep(5)
    def test_open_user_group_page(self):
        UserGroupPage().open_and_check()



if __name__ == '__main__':
    unittest.main()
