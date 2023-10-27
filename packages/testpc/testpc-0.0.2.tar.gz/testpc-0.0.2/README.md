# 介绍

[Gitee](https://gitee.com/bluepang2021/testpc_project)

PC UI automation testing framework based on pytest.

> 基于pytest 的 PC UI自动化测试框架

## 特点

* 集成`pyautogui`
* 集成`allure`, 支持HTML格式的测试报告
* 提供强大的`数据驱动`，支持json、yaml
* 提供丰富的断言
* 支持生成随机测试数据
* 支持设置用例依赖


## 三方依赖

* Allure：https://github.com/allure-framework/allure2

## Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple testpc
```

## 🤖 Quick Start

1、查看帮助：
```shell
testpc --help
Usage: testpc [OPTIONS]

Options:
  --version               Show version.
  -p, --projectName TEXT  Create demo by project name
  --help                  Show this message and exit.
```

2、运行项目：

* ✔️ 在`pyCharm`中右键执行(需要把项目的单元测试框架改成unittests)

* ✔️ 通过命令行工具执行。

3、查看报告

运行`allure server report`浏览器会自动调起报告（需先安装配置allure）


## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解testpc的用法。

* page类

```python
from testpc import Page, ImageElem, CoorElem


class MacPage(Page):
    """根据图片定位，建议使用系统自带截图（shift+command+4）"""

    num_3 = ImageElem(image='../data/calculator_3.png', desc="数字3")
    x = ImageElem(image='../data/calculator_x.png', desc="乘以号")
    num_5 = ImageElem(image='../data/calculator_5.png', desc="数字5")
    equal = ImageElem(image='../data/calculator_=.png', desc="等于")


class MacPage1(Page):
    """根据坐标定位，可以使用MacDriver的get_location方法实时获取"""
    num_3 = CoorElem(coor=(1785, 364), desc="数字3")
    x = CoorElem(coor=(1833, 369), desc="乘以号")
    num_5 = CoorElem(coor=(1720, 316), desc="数字3")
    equal = CoorElem(coor=(1869, 404), desc="等于")
```

* 用例类

```python
import testpc

from pages.mac_page import MacPage


class TestMacDemo(testpc.TestCase):
    """Mac应用demo"""

    def start(self):
        self.mac_page = MacPage(self.driver)

    def test_1(self):
        self.mac_page.num_3.click()
        self.mac_page.x.click()
        self.mac_page.num_5.click()
        self.mac_page.equal.click()
        self.driver.screenshot("计算结果")


if __name__ == '__main__':
    """仅执行本模块"""
    testpc.main(pkg_name='Calculator')
```

### 参数化

```python
import testpc
from testpc import logger


LIST_DATA = [
    {"name": "李雷", "age": "33"},
    {"name": "韩梅梅", "age": "30"}
]


class TestParameter(testpc.TestCase):
    """
    参数化demo
    """

    @testpc.data(LIST_DATA)
    def test_list(self, param):
        logger.info(param)

    @testpc.file_data(file='../data/data.json')
    def test_json(self, param):
        logger.info(param)

    @testpc.file_data(file='../data/data.yml', key='names')
    def test_yaml(self, param):
        print(param)


if __name__ == '__main__':
    testpc.main()
```

### Run the test

```python
import testpc

testpc.main()  # 当前文件，pycharm中需要把默认的单元测试框架改成unittests
testpc.main(case_path="./")  # 当前目录
testpc.main(case_path="./test_dir/")  # 指定目录
testpc.main(case_path="./test_dir/test_api.py")  # 指定特定文件
testpc.main(case_path="./test_dir/test_api.py::TestCaseClass:test_case1") # 指定特定用例
```

### 感谢

感谢从以下项目中得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

* [PyAutoGUI]

## 高级用法

### 随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

kuto 提供了随机获取测试数据的方法。

```python
import testpc
from testpc import testdata


class TestYou(testpc.TestCase):
    
    def test_case(self):
        """a simple tests case """
        word = testdata.get_word()
        print(word)
        
if __name__ == '__main__':
    testpc.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

**更多的方法**

```python
from testpc.testdata import *
# 随机一个名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))
print("名字(中文男)：", first_name(gender="male", language="zh"))
print("名字(中文女)：", first_name(gender="female", language="zh"))
# 随机一个姓
print("姓:", last_name())
print("姓(中文):", last_name(language="zh"))
# 随机一个姓名
print("姓名:", username())
print("姓名(中文):", username(language="zh"))
# 随机一个生日
print("生日:", get_birthday())
print("生日字符串:", get_birthday(as_str=True))
print("生日年龄范围:", get_birthday(start_age=20, stop_age=30))
# 日期
print("日期(当前):", get_date())
print("日期(昨天):", get_date(-1))
print("日期(明天):", get_date(1))
# 数字
print("数字(8位):", get_digits(8))
# 邮箱
print("邮箱:", get_email())
# 浮点数
print("浮点数:", get_float())
print("浮点数范围:", get_float(min_size=1.0, max_size=2.0))
# 随机时间
print("当前时间:", get_now_datetime())
print("当前时间(格式化字符串):", get_now_datetime(strftime=True))
print("未来时间:", get_future_datetime())
print("未来时间(格式化字符串):", get_future_datetime(strftime=True))
print("过去时间:", get_past_datetime())
print("过去时间(格式化字符串):", get_past_datetime(strftime=True))
# 随机数据
print("整型:", get_int())
print("整型32位:", get_int32())
print("整型64位:", get_int64())
print("MD5:", get_md5())
print("UUID:", get_uuid())
print("单词:", get_word())
print("单词组(3个):", get_words(3))
print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))
```

* 运行结果

```shell
名字： Hayden
名字（男）： Brantley
名字（女）： Julia
名字（中文男）： 觅儿
名字（中文女）： 若星
姓: Lee
姓（中文）: 白
姓名: Genesis
姓名（中文）: 廉高义
生日: 2000-03-11
生日字符串: 1994-11-12
生日年龄范围: 1996-01-12
日期（当前）: 2022-09-17
日期（昨天）: 2022-09-16
日期（明天）: 2022-09-18
数字(8位): 48285099
邮箱: melanie@yahoo.com
浮点数: 1.5315717275531858e+308
浮点数范围: 1.6682402084146244
当前时间: 2022-09-17 23:33:22.736031
当前时间(格式化字符串): 2022-09-17 23:33:22
未来时间: 2054-05-02 11:33:47.736031
未来时间(格式化字符串): 2070-08-28 16:38:45
过去时间: 2004-09-03 12:56:23.737031
过去时间(格式化字符串): 2006-12-06 07:58:37
整型: 7831034423589443450
整型32位: 1119927937
整型64位: 3509365234787490389
MD5: d0f6c6abbfe1cfeea60ecfdd1ef2f4b9
UUID: 5fd50475-2723-4a36-a769-1d4c9784223a
单词: habitasse
单词组（3个）: уж pede. metus.
手机号: 13171039843
手机号(移动): 15165746029
手机号(联通): 16672812525
手机号(电信): 17345142737
```

### 用例的依赖

**depend**

`depend` 装饰器用来设置依赖的用例。

```python
import testpc
from testpc import depend


class TestDepend(testpc.TestCase):
    
    @depend(name='test_001')
    def test_001(self):
        print("test_001")
        
    @depend("test_001", name='test_002')
    def test_002(self):
        print("test_002")
        
    @depend(["test_001", "test_002"])
    def test_003(self):
        print("test_003")
        
if __name__ == '__main__':
    testpc.main()
```

* 被依赖的用例需要用name定义被依赖的名称，因为本装饰器是基于pytest.mark.dependency，它会出现识别不了被装饰的方法名的情况
  ，所以通过name强制指定最为准确
  ```@depend(name='test_001')```
* `test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。
* 如果依赖多个用例，传入一个list即可
```@depend(['test_001', 'test_002'])```
  
### 发送邮件

```python
import testpc
from testpc.utils.mail import Mail


if __name__ == '__main__':
    testpc.main()
    mail = Mail(host='xx.com', user='xx@xx.com', password='xxx')
    mail.send_report(title='Demo项目测试报告', report_url='https://www.baidu.com', to_list=['xx@xx.com'])
```

- title：邮件标题
- report_url: 测试报告的url
- to_list: 接收报告的用户列表


### 发送钉钉

```python
import testpc
from testpc.utils.dingtalk import DingTalk


if __name__ == '__main__':
    testpc.main()
    dd = DingTalk(secret='xxx',
                  url='xxx')
    dd.send_report(msg_title='Demo测试消息', report_url='https://www.baidu.com')
```

- `secret`: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
- `url`: 钉钉机器人的Webhook链接
- `msg_title`: 消息标题
- `report_url`: 测试报告url



