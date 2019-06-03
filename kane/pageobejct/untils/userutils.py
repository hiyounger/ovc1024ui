# -*- encoding:utf-8 -*-

from kane.pageobejct.loginpage import LoginPage

class UserUtils():

    @classmethod
    def login(cls,email,password):
        LoginPage().login(email,password)