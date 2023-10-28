"""
@Author: kang.yang
@Date: 2023/9/20 10:53
"""
from testpc import Page, ImageElem


class WinPage(Page):
    num_3 = ImageElem(image='../data/calculator_3_win.png', desc="数字3")
    x = ImageElem(image='../data/calculator_x_win.png', desc="乘以号")
    num_5 = ImageElem(image='../data/calculator_5_win.png', desc="数字5")
    equal = ImageElem(image='../data/calculator_=_win.png', desc="等于")
