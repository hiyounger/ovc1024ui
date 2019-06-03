# -*- encoding:utf-8 -*-

from kane.pageobejct.loginpage import LoginPage

class UserUtils():

    @classmethod
    def login(cls,email,password):
        loginPage = LoginPage()
        loginPage.open_and_check()
        loginPage.login(email, password)