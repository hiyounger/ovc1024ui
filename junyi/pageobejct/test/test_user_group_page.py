import unittest

from junyi.pageobejct.utils.userutils import UserUtils
from junyi.pageobejct.user_group_page import UserGroupPage
import time


class TestUserGroupPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        username = 'qsong.vip@qq.com'
        password = 'hiyounger888'
        UserUtils.login(username, password)
        time.sleep(5)

    def test_open_user_group_page(self):
        UserGroupPage().open_and_check()


if __name__ == '__main__':
    unittest.main()
