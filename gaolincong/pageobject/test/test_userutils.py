# -*- encoding:utf-8 -*-
from gaolincong.pageobject.utils.userutils import UserUtils
import unittest


class MyTestUserutils(unittest.TestCase):
    def test_userutils(self):
        username='1690344964@qq.com'
        password='6149762364'
        UserUtils().Login(username,password)


if __name__ == '__main__':
    unittest.main()
