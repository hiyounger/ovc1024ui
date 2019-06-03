# -*- encoding:utf-8 -*-
from selenium import webdriver
from laijunchen.utils.abs import Singleton

@Singleton
class FireFoxDirver():
    __dirver = None

    def __init__(self):
        if self.__dirver == None:
            self.__dirver =webdriver.Firefox()

    def get_dirver(self):
        return self.__dirver