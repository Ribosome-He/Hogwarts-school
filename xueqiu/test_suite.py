# -*- coding: utf-8 -*-

import unittest
from common import HTMLTestRunner
import sys,os,time


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

def caseList():
    list = path + r"\cases"
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(list,pattern='*Test.py')
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit

def test_report():

    alltest = caseList()

    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    filename = path+r'\result\\'+now+'result.html'
    fp = open(filename, 'wb')

    #runner = HTMLTestRunner(output=path+r'\result\\',stream=fp,report_title=u'test report',descriptions=u'description')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'test report', description=u'description')

    runner.run(alltest)

    fp.close()

if __name__ == "__main__":
    test_report()