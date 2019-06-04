# -*- encoding:utf-8 -*-
from gaolincong.pageobject.loginpage import Login

class UserUtils():
    @classmethod
    def Login(cls,email,pwd):
        login=Login()
        login.open_and_check()
        login.login(email,pwd)