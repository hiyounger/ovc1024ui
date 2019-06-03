# -*- encoding:utf-8 -*-
from yushiqian.pageobject.loginpage import LoginPage

class UserUtils():


    def login(cls, email, password):
        LoginPage().login(email, password)

