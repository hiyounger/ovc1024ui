# -*- encoding:utf-8 -*-
import unittest

from junyi.pageobejct.utils.userutils import UserUtils
from junyi.pageobejct.user_group_page import UserGroupPage
from junyi.pageobejct.user_group_create_page import UserGroupCreatePage

class TestUserGroupCases(unittest.TestCase):

    def test_case_258(self):
        # 前置条件
        #1. 用户登录成功
        UserUtils.login('qsong.vip@qq.com', 'hiyounger888')
        #2. 打开小组页面
        UserGroupPage().open_and_check()
        UserGroupPage().create_group_button.click()

        #测试步骤
        act_result = UserGroupCreatePage().check_if_page_open()
        self.assertTrue(act_result)


if __name__ == '__main__':
    unittest.main()
