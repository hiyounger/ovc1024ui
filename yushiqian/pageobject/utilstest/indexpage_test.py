import unittest
from yushiqian.pageobject.indexpage import Userutils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        email="763208734@qq.com"
        password="yu75321ysq"
        Userutils.login(email, password)


if __name__ == '__main__':
    unittest.main()
