import unittest
from kuang.pageobjct.utils.userutils import UserUtils

class TestUserUtils(unittest.TestCase):
    def test_userlogin(self):
        username ='kujipi@qq.com'
        password='kjp19920630'
        UserUtils.login(username,password)


if __name__ == '__main__':
    unittest.main()
