# -*- coding: utf-8 -*-
from selenium.webdriver.common.touch_actions import TouchActions
from  .base_page import BasePage
from .profile_page import ProfilePage
from .search_page import SearchPage
import common.startset

class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def gotoProfile(self):
        self.by_id("user_profile_icon").click()
        return ProfilePage(self.driver)

    def gotoSearch(self):
        self.by_id("home_search").click()
        return SearchPage(self.driver)

