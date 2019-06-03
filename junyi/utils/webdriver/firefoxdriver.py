# -*- encoding:utf-8 -*-
from selenium import webdriver
from junyi.utils.abs import Singleton


@Singleton
class FirefoxDriver():

    __driver = None

    def __init__(self):
        if self.__driver == None:
            self.__driver = webdriver.Firefox()

    def get_driver(self):
        return self.__driver
