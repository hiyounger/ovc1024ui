import unittest
from kane.pageobejct.untils.userutils import UserUtils


class TestUserUtils(unittest.TestCase):

    def test_userlogin(self):
        username = "352093042@qq.com"
        password = "zsefbji3069"
        UserUtils.login(username,password)


if __name__ == '__main__':
    unittest.main()
