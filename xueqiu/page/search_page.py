# -*- coding: utf-8 -*-
from  .base_page import BasePage
import selenium.webdriver.common.by

class SearchPage(BasePage):
    def __init__(self,driver):
        super(SearchPage,self).__init__(driver)

    def search(self,key):
        self.by_id("search_input_text").send_keys(key)

    def cancel(self):
        self.by_id("action_close").click()

    def getAll(self):
        a=[]
        list = self.driver.find_elements("xpath","//*[contains(@resource-id, 'stockName')]")
        for n in list:
            a.append(n.text)
        return a

    def guanzhu(self):
        self.find_xpath("//*[@resource-id='com.xueqiu.android:id/add_attention']").\
            find_element_by_class_name("android.widget.TextView").click()

    def zixuanguanzhu(self):
        self.find_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element_by_id("action_create_cube").click()