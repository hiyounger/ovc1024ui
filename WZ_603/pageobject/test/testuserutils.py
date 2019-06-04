import unittest

from WZ_603.pageobject.utils.userutil import UserUtills


class TestUserUtils(unittest.TestCase):

    def test_userlogin(self):
        username = 'qsong.vip@qq.com'
        password = 'hiyounger888'
        UserUtills.login(username, password)


if __name__ == '__main__':
    unittest.main()
