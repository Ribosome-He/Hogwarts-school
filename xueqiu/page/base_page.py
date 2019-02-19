# -*- coding: utf-8 -*-
import re
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver


    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)

    def by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_xpath_name(self, xpath_name):
        return self.driver.find_element_by_xpath(xpath_name)

    def by_xpath_text(self, content):
        return self.driver.find_element_by_xpath(("//*[@text='"+ content + "']"))

    def screenshot(self, screenshot_name):
        return self.driver.save_screenshot(screenshot_name)

    def find(self,value):
        if re.search(r"/.*",value):
            by = "xpath"
        else:
            by = "id"
        try:
            return self.driver.find_element(by, value)
        except Exception as e:
            print("can not find this element" + e)
            try:
                self.by_xpath_text("下次再说").click()
            except Exception as e:
                print("unknow error" + e)
            return self.driver.find_element(by, value)

