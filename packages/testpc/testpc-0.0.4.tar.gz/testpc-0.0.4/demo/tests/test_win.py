"""
@Author: kang.yang
@Date: 2023/9/20 10:54
"""
import testpc

from pages.win_page import WinPage


class TestMacDemo(testpc.TestCase):

    def start(self):
        self.win_page = WinPage(self.driver)

    def test_1(self):
        self.win_page.num_3.click()
        self.win_page.x.click()
        self.win_page.num_5.click()
        self.win_page.equal.click()
        self.driver.screenshot("计算结果")


if __name__ == '__main__':
    # 仅执行本模块
    testpc.main(pkg_name='calc.exe')

