# -*- encoding:utf-8 -*-

from junyi.pageobejct.loginpage import LoginPage


class UserUtils():

    @classmethod
    def login(cls, email, password):
        loginPage = LoginPage()
        loginPage.open_and_check()
        loginPage.login(email, password)


