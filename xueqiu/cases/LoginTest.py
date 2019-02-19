# -*- coding: utf-8 -*-
import unittest
import time,sys

from common import startset
from page import login_page,main_page


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = startset.StartSet().get_driver()

    def test_loginfaile(self):
        self.MainPage = main_page.MainPage(self.driver)
        self.ProfilePage = self.MainPage.gotoProfile()
        self.LoginPage = self.ProfilePage.gotoLogin()

        self.LoginPage.other_login()

        self.LoginPage.password_login()

        self.LoginPage.send_username("136824780844")

        self.LoginPage.send_password("0000000")

        self.LoginPage.click_login()

        message = self.LoginPage.get_message()
        self.assertEqual(message,"手机号码填写错误")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
