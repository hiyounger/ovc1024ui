# -*- encoding:utf-8 -*-

from laijunchen.pageobject.loginpage import LoginPage

class UserUtils():

    @classmethod
    def login(cls, eamil, password):
        loginpage = LoginPage()
        loginpage.open_and_check()
        loginpage.login(eamil, password)
