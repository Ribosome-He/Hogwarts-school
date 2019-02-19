# -*- coding: utf-8 -*-
import unittest
import time,sys,os
import ddt

from common import startset
from page import main_page

path = os.getcwd()
@ddt.ddt
class SearchCase(unittest.TestCase):
    def setUp(self):
        self.driver = startset.StartSet().get_driver()
        self.MainPage = main_page.MainPage(self.driver)
        self.SearchPage = self.MainPage.gotoSearch()

    @ddt.file_data(path+r"\data\searchdata.json")
    def test_checksearch(self,value):
        self.SearchPage.search(value[0])

        name = self.SearchPage.getAll()[0]
        print(name)
        self.assertEqual(name,value[1])
        self.SearchPage.cancel()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()