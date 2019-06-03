# -*- encoding:utf-8 -*-

from junyi.pageobejct.loginpage import LoginPage

class UserUtils():

    @classmethod
    def login(cls, email, password):
        LoginPage().login(email, password)


