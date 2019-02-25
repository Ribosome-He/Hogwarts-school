from appium import webdriver
import pytest
import time


class Test_xueqiu(object):
    @pytest.fixture(scope='function', autouse=True)
    def startDriver(self):
        self.caps = {}
        self.caps["platformName"] = "Android"
        self.caps["platformVersion"] = "4.4"
        self.caps["deviceName"] = "127.0.0.1:62001"
        self.caps["appActivity"] = ".view.WelcomeActivityAlias"
        self.caps["appPackage"] = "com.xueqiu.android"

        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub',self.caps)
        self.driver.implicitly_wait("6")

        yield
        self.driver.quit()


#封装find方法，处理有时候会弹出的评价弹框
    def find_xpath(self,value):
        loclist = []
        try:
            for n in range(5):
                time.sleep(1)
                ele = self.driver.find_element_by_xpath(value)
                loclist.append(ele.location)
                if n>1:
                    if loclist[n] == loclist[n-1]:
                        return ele
        except:
            print("出现评价弹框")
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
            print("点击下次再说")
            return self.driver.find_element_by_xpath(value)


    def test_pdd(self):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("pdd")
        self.driver.find_elements("xpath", "//*[contains(@resource-id, 'stockName')]")[0].click()

    def test_alibaba(self):
        self.find_xpath("//*[@text='自选']").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        assert self.find_xpath("//*[contains(@resource-id, 'stockName')]").text == "阿里巴巴"
        self.find_xpath("//*[contains(@resource-id, 'follow_btn')]").click()
        time.sleep(4)
        self.find_xpath("//*[@text='取消']").click()
        try:
            self.driver.find_element_by_id("iv_close").click()
        except:
            pass
        assert self.find_xpath( "//*[contains(@text, '阿里巴巴')]")



if __name__ == "__main__":
    pytest.main("-s  test_xueqiu.py")