# -*- coding: utf-8 -*-
from appium import webdriver
import json,sys,os

class StartSet():
    def __init__(self):
        self.path = os.getcwd()
        with open(self.path + "\data\globalconfig.json", "r", encoding="UTF-8") as f:
            jsoncaps = json.load(f)
        self.caps = jsoncaps["capabilities"]
        # self.caps["platformName"] = "Android"
        # self.caps["platformVersion"] = "4.4"
        # # self.caps["deviceName"] = "T8DDU15B26001191"
        # self.caps["deviceName"] = "127.0.0.1:62001"
        # self.caps["appActivity"] = ".view.WelcomeActivityAlias"
        # self.caps["appPackage"] = "com.xueqiu.android"

        self.driver = webdriver.Remote(jsoncaps["url"], self.caps)
        self.driver.implicitly_wait(jsoncaps["wait"])

    def get_driver(self):
        return self.driver