from xpinyin import Pinyin
import pytest

a = Pinyin()
#tone_marks参数测试
# print("tone_marks  test")
# print(a.get_pinyin())
# print(a.get_pinyin('marks'))
# print(a.get_pinyin(tone_marks='numbers'))
# print(a.get_pinyin(tone_marks='other'))
# print(a.get_pinyin(tone_marks=''))
#
# print(" ")
#
# print("convert  test")
print(a.get_pinyin(chars="肾zhen",tone_marks='numbers',convert='capitalize'))
print(a.get_pinyin(chars="深圳",tone_marks='marks',convert='upper'))
# print(a.get_pinyin(convert='lower'))
#
#
# print(" ")
#
# print("splitter  test")
# print(a.get_pinyin(splitter=u'+'))
#
# print(" ")
#
# print("chars test")
# print(a.get_pinyin(chars="前田敦子"))

print(a.get_initial("F"))
print(a.get_initials("芳芳"))



def test_get_pinyin_defult():
    result = Pinyin().get_pinyin()
    assert result == "ni-hao"

@pytest.mark.parametrize("chars,tone_marks,convert",[
    ("深圳",None,'lower','ni-hao'),
    ("深圳",'marks','upper','NǏ-HǍO'),
    ("深圳",'numbers','capitalize','Ni3-Hao3'),
])
def test_get_pinyin(chars,tone_marks,convert,value):
    assert Pinyin().get_pinyin(chars=chars,tone_marks=tone_marks,convert=convert) == value
