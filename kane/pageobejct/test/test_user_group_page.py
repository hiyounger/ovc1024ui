import unittest
from kane.pageobejct.untils.userutils import UserUtils
from kane.pageobejct.user_group_page import UserGruopPage
import time

class TestUserGroupPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        username = "352093042@qq.com"
        password = "zsefbji3069"
        UserUtils.login(username,password)
        time.sleep(5)

    def test_open_user_group_page(self):
        UserGruopPage().open_and_check()

if __name__ == '__main__':
    unittest.main()