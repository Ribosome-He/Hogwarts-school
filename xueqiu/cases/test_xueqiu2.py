from appium import webdriver
import pytest
import time
from appium.webdriver.common.touch_action import TouchAction
from page import main_page


class Test_xueqiu(object):
    @pytest.fixture(scope='function', autouse=True)
    def startDriver(self):
        self.caps = {}
        self.caps["platformName"] = "Android"
        self.caps["platformVersion"] = "4.4"
        self.caps["deviceName"] = "127.0.0.1:62001"
        self.caps["appActivity"] = ".view.WelcomeActivityAlias"
        self.caps["appPackage"] = "com.xueqiu.android"
        self.caps["unicodeKeyboard"] = True
        self.caps["resetKeyboard"] = True
        #self.caps["automationName"] = "UiAutomator2"

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

    def test_search_add(self):
        self.find_xpath("//*[@text='自选']").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        assert self.find_xpath("//*[contains(@resource-id, 'stockName')]").text == "阿里巴巴"
        self.find_xpath("//*[contains(@resource-id, 'follow_btn')]").click()
        #time.sleep(2)
        self.find_xpath("//*[@text='取消']").click()
        try:
            self.driver.find_element_by_id("iv_close").click()
        except:
            pass
        assert self.find_xpath("//*[contains(@text, '阿里巴巴')]")

    def test_alibaba_search(self):
        self.find_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")
        before_ele = self.find_xpath("//*[@resource-id='com.xueqiu.android:id/add_attention']").find_element_by_class_name("android.widget.TextView")
        before = before_ele.get_attribute("resourceId")
        #使用xpath定位resource-id，resource-id要写全，获取这个属性后也是全的
        before_ele.click()
        after = self.find_xpath("//*[@resource-id='com.xueqiu.android:id/add_attention']").\
            find_element_by_class_name("android.widget.TextView").get_attribute("resourceId")
        assert before != after

    def test_alibaba_exist(self):
        self.find_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        stocktext = self.is_exist()
        assert "阿里巴巴" in stocktext

    def is_exist(self):
        stockName_list = self.driver.find_elements_by_id("portfolio_stockName")
        stocktext = []
        if len(stockName_list) > 0:
            for n in stockName_list:
                stocktext.append(n.text)
        return stocktext

    def test_add_us(self):
        self.find_xpath("//*[@text='行情' and contains(@resource-id,'tab_name')]").click()
        self.find_xpath("//*[@text='美股']").click()
        self.find_xpath("//*[@text='美股']").click()
        ele = self.find_xpath("//*[contains(@resource-id,'stock_code')]/..//*[contains(@resource-id,'stock_name')]")
        eleName = ele.text
        ele.click()
        self.find_xpath("//*[@text='加自选']").click()
        self.find_xpath("//*[contains(@resource-id,'action_back')]").click()
        #self.driver.back()
        self.find_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        stocktext = self.is_exist()
        assert eleName in stocktext

    def test_delete_us(self):
        self.find_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        self.find_xpath("//*[@text='美股']").click()
        ele = self.find_xpath("//*[contains(@resource-id,'portfolio_stockName')]")
        eleName = ele.text
        TouchAction(self.driver).long_press(ele).perform()
        self.find_xpath("//*[@text='删除']").click()
        stocktext = self.is_exist()
        assert eleName not in stocktext

    @pytest.mark.parametrize("stockname",
        [
        "百度", "阿里巴巴", "腾讯", "美团", "今日头条",
        "拼多多", "饿了么", "京东", "滴滴出行", "中国平安",
        "中国联通", "中国移动", "Facebook", "Google", "大疆",
        "雅虎", "微软", "高通", "小米", "格力",
        "oppo", "vivo手机", "苹果", "美的", "恒大",
        "蚂蚁金服", "网易", "陌陌", "中国人保", "京东方"

        ])
    def test_add_batch(self,stockname):
        self.find_xpath("//*[@text='自选']").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys(stockname)
        before_ele = self.find_xpath("//*[@resource-id='com.xueqiu.android:id/add_attention']").find_element_by_class_name("android.widget.TextView")
        if before_ele.get_attribute("resourceId") == "com.xueqiu.android:id/follow_btn":
            before_ele.click()
        else:
            print("已关注")

    @pytest.fixture(scope='function', autouse=True)
    def setUpdriver(self):
        self.driver = startset.StartSet().get_driver()
        self.MainPage = main_page.MainPage(self.driver)
        self.SearchPage = self.MainPage.gotoSearch()

    def test_zixuan(self,key):
        self.SearchPage.zixuanguanzhu()
        self.SearchPage.search("阿里巴巴")
        self.SearchPage.guanzhu()