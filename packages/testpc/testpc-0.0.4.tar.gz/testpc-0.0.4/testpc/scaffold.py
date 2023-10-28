import os.path
import platform


case_mac_content = """import testpc

from pages.mac_page import MacPage


class TestMacDemo(testpc.TestCase):

    def start(self):
        self.mac_page = MacPage(self.driver)

    def test_1(self):
        self.mac_page.num_3.click()
        self.mac_page.x.click()
        self.mac_page.num_5.click()
        self.mac_page.equal.click()
        self.driver.screenshot("计算结果")


if __name__ == '__main__':
    testpc.main(pkg_name='Calculator')
"""

case_win_content = """import testpc

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
"""

page_mac_content = """from testpc import Page, ImageElem, CoorElem


class MacPage(Page):
    # 根据图片定位，建议使用系统自带截图（shift+command+4)

    num_3 = ImageElem(image='../data/calculator_3.png', desc="数字3")
    x = ImageElem(image='../data/calculator_x.png', desc="乘以号")
    num_5 = ImageElem(image='../data/calculator_5.png', desc="数字5")
    equal = ImageElem(image='../data/calculator_=.png', desc="等于")


class MacPage(Page):
    # 根据坐标定位，可以使用MacDriver的get_location方法实时获取
    num_3 = CoorElem(coor=(1785, 364), desc="数字3")
    x = CoorElem(coor=(1833, 369), desc="乘以号")
    num_5 = CoorElem(coor=(1720, 316), desc="数字3")
    equal = CoorElem(coor=(1869, 404), desc="等于")
"""

page_win_content = """from testpc import Page, ImageElem


class WinPage(Page):
    num_3 = ImageElem(image='../data/calculator_3_win.png', desc="数字3")
    x = ImageElem(image='../data/calculator_x_win.png', desc="乘以号")
    num_5 = ImageElem(image='../data/calculator_5_win.png', desc="数字5")
    equal = ImageElem(image='../data/calculator_=_win.png', desc="等于")
"""

run_content = """import testpc


if __name__ == '__main__':

    testpc.main(
        case_path="tests/test_mac.py",
        pkg_name="Calculator"
    )
"""


def create_scaffold(projectName):
    """create scaffold with specified project name."""

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    # 新增测试数据目录
    root_path = projectName
    create_folder(root_path)
    create_folder(os.path.join(root_path, "tests"))
    create_folder(os.path.join(root_path, "pages"))
    create_folder(os.path.join(root_path, "report"))
    create_folder(os.path.join(root_path, "data"))
    create_folder(os.path.join(root_path, "screenshot"))
    if platform.system() == 'Windows':
        create_file(
            os.path.join(root_path, "tests", "test_win.py"),
            case_win_content,
        )
        create_file(
            os.path.join(root_path, "pages", "win_page.py"),
            page_win_content,
        )
    else:
        create_file(
            os.path.join(root_path, "tests", "test_mac.py"),
            case_mac_content,
        )
        create_file(
            os.path.join(root_path, "pages", "mac_page.py"),
            page_mac_content,
        )
    create_file(
        os.path.join(root_path, "run.py"),
        run_content,
    )
