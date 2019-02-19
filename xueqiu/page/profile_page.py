# -*- coding: utf-8 -*-
from  .base_page import BasePage
from .login_page import LoginPage

class ProfilePage(BasePage):
    def __init__(self,driver):
        super(ProfilePage, self).__init__(driver)

    def gotoLogin(self):
        self.by_id("tv_login").click()
        return LoginPage(self.driver)