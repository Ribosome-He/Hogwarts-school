# -*- coding: utf-8 -*-
from  .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
       # self.passwordLogin = self.by_xpath_name("//*[@text='邮箱手机号密码登录']")

    def other_login(self):
        self.other = self.by_id("tv_login_by_phone_or_others")
        return self.other.click()

    def password_login(self):
        self.passwordLogin = self.by_id("tv_login_with_account")
        return self.passwordLogin.click()

    def send_username(self,username):
        self.username = self.by_id("login_account")
        return self.username.send_keys(username)

    def send_password(self,password):
        self.password = self.by_xpath_name("//*[@password='true']")
        return  self.password.send_keys(password)

    def click_login(self):
        self.login = self.by_id("button_next")
        return self.login.click()

    def get_message(self):
        self.msg = self.by_id("md_content")
        message = self.msg.text
        return message

    def click_ok(self):
        return self.by_id("md_buttonDefaultPositive").click()

    def LoginFaile(self,username,password):
        self.other.click()
        self.passwordLogin.click()
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login.click()
        #msg1 = self.msg.text()
        self.click_ok()
