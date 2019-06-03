import unittest

from junyi.pageobejct.utils.userutils import UserUtils


class TestUserUtils(unittest.TestCase):

    def test_userlogin(self):
        username = 'qsong.vip@qq.com'
        password = 'hiyounger888'
        UserUtils.login(username, password)


if __name__ == '__main__':
    unittest.main()
