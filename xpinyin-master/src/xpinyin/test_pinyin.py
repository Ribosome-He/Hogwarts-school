from xpinyin import Pinyin
import pytest
import allure
import os


@allure.feature('test_get_pinyin')
@allure.story('test_defult')
@allure.severity('blocker')
@allure.issue("www.baidu.com")
def test_get_pinyin_defult():
    with allure.step('默认参数'):
        result = Pinyin().get_pinyin()
        assert result == "ni-hao"


@allure.feature('test_get_pinyin')
@allure.story('test_chars_marks_convert')
@pytest.mark.parametrize("chars,tone_marks,convert,value",[
    ("深圳",None,'lower','shen-zhen'),
    ("深圳",'marks','upper','SHĒN-ZHÈN'),
    ("深圳",'numbers','capitalize','Shen1-Zhen4'),
    ("shenzhen",'numbers','capitalize','shen1zhen'),
    ("深zhen",'numbers','capitalize','Shen1-zhen')
])
def test_get_pinyin(chars,tone_marks,convert,value):
    with allure.step('修改marks参数'):
        result = Pinyin().get_pinyin(chars=chars,tone_marks=tone_marks,convert=convert)
        path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")),"img/timg.jpg")  #获取当前脚本文件的绝对路径
        file = open(path,'rb').read()
        allure.attach('test_img',file,allure.attach_type.JPG)
        assert result == value


@allure.feature('test_get_pinyin')
@allure.story('test_split')
@pytest.mark.parametrize("splitter,value",[(u'+',"ni+hao"),(u'*',"ni*hao")])
def test_get_pinyin_split(splitter,value):
    assert Pinyin().get_pinyin(splitter=splitter) == value


@allure.feature('test_get_initial')
@pytest.mark.parametrize("chars,value",[("芳","F"),("F","F")])
def test_get_initial(chars,value):
    assert Pinyin().get_initial(chars) == value


@allure.feature('test_get_initial')
@pytest.mark.parametrize("chars,value",[("芳芳","F-F"),("F芳","F-F"),("芳F","F-F")])
def test_get_initials(chars,value):
    assert Pinyin().get_initials(chars) == value
