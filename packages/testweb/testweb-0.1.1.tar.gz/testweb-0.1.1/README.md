# 介绍

[Gitee](https://gitee.com/bluepang2021/testweb_project)

WebUI/HTTP automation testing framework based on pytest.

> 基于pytest 的 Web UI/HTTP自动化测试框架

## 特点

* 集成`playwright`/`requests`
* 集成`allure`, 支持HTML格式的测试报告
* 提供强大的`数据驱动`，支持json、yaml
* 提供丰富的断言
* 支持生成随机测试数据
* 支持设置用例依赖


## 三方依赖

* Allure：https://github.com/allure-framework/allure2

## Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple testweb
```

## 🤖 Quick Start

1、查看帮助：
```shell
Usage: testweb [OPTIONS]

Options:
  --version               Show version.
  -i, --install           Install the browser driver.
  -p, --projectName TEXT  Create demo by project name
  --help                  Show this message and exit.
```

2、运行项目：

* ✔️ 在`pyCharm`中右键执行(需要把项目的单元测试框架改成unittests)

* ✔️ 通过命令行工具执行。

3、查看报告

运行`allure server report`浏览器会自动调起报告（需先安装配置allure）


## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解testweb的用法。


* page类

```python
from testweb import Page, Elem

'''
url相同的页面定义为同一个页面
定位方式：优先使用css，大规模开展自动化前需要开发给相关元素加上唯一标识的测试id
css: 根据cssSelector进行定位，https://zhuanlan.zhihu.com/p/571510714
xpath: 根据xpath进行定位，教程：https://zhuanlan.zhihu.com/p/571060826
text: 根据元素的可视文本内容进行定位
holder: 根据输入框placeHolder进行定位
index: 获取第index个定位到的元素
'''


class IndexPage(Page):
    # 首页
    loginBtn = Elem(text='登录/注册', desc='登录/注册按钮')
    patentText = Elem(text='查专利', desc='查专利文本')


class LoginPage(Page):
    # 登录页
    pwdLoginTab = Elem(text='帐号密码登录', desc='账号密码登录tab')
    userInput = Elem(holder='请输入手机号码', desc='账号输入框')
    pwdInput = Elem(holder='请输入密码', desc='密码输入框')
    licenseBtn = Elem(css="span.el-checkbox__inner", index=1, desc='协议选择按钮')
    loginBtn = Elem(text='立即登录', desc='立即登录按钮')
    firstCompanyIcon = Elem(xpath="(//img[@class='right-icon'])[1]", desc='第一家公司')
```

* 公共方法

```python
from page.web_page import IndexPage, LoginPage


class Pub(object):
    """公共方法"""

    def __init__(self, driver):
        self.driver = driver
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def pwd_login(self, username="13652435335", password="wz123456@QZD"):
        """账号密码登录流程"""
        self.index_page.loginBtn.click()
        self.login_page.pwdLoginTab.click()
        self.login_page.userInput.input(username)
        self.login_page.pwdInput.input(password)
        self.login_page.licenseBtn.click()
        self.login_page.loginBtn.click()
        self.login_page.firstCompanyIcon.click()
```

* 用例类

```python
import testweb

from pub import Pub


class TestWebDemo(testweb.TestCase):

    def start(self):
        self.pub = Pub(self.driver)

    @testweb.title("登录")
    def test_login(self):
        self.open_url()
        self.pub.pwd_login()
        self.assert_url()
        self.screenshot("首页")


if __name__ == '__main__':
    testweb.main(host="https://www-test.qizhidao.com")
```

### 参数化

```python
import testweb


LIST_DATA = [
    {"name": "李雷", "age": "33"},
    {"name": "韩梅梅", "age": "30"}
]


class TestParameter(testweb.TestCase):
    """
    参数化demo
    """

    @testweb.data(LIST_DATA)
    def test_list(self, param):
        testweb.logger.info(param)

    @testweb.file_data(file='../static/data.json')
    def test_json(self, param):
        testweb.logger.info(param)

    @testweb.file_data(file='../static/data.yml', key='names')
    def test_yaml(self, param):
        print(param)


if __name__ == '__main__':
    testweb.main()
```

### Run the test

```python
import testweb

testweb.main()  # 当前文件，pycharm中需要把默认的单元测试框架改成unittests
testweb.main(case_path="./")  # 当前目录
testweb.main(case_path="./test_dir/")  # 指定目录
testweb.main(case_path="./test_dir/test_api.py")  # 指定特定文件
testweb.main(case_path="./test_dir/test_api.py::TestCaseClass:test_case1") # 指定特定用例
```

### 感谢

感谢从以下项目中得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

* [playwright](https://github.com/microsoft/playwright-python)


## 高级用法

### 随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

kuto 提供了随机获取测试数据的方法。

```python
import testweb
from testweb import testdata


class TestYou(testweb.TestCase):
    
    def test_case(self):
        """a simple tests case """
        word = testdata.get_word()
        print(word)
        
if __name__ == '__main__':
    testweb.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

**更多的方法**

```python
from testweb.testdata import *
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
import testweb
from testweb import depend


class TestDepend(testweb.TestCase):
    
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
    testweb.main()
```

* 被依赖的用例需要用name定义被依赖的名称，因为本装饰器是基于pytest.mark.dependency，它会出现识别不了被装饰的方法名的情况
  ，所以通过name强制指定最为准确
  ```@depend(name='test_001')```
* `test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。
* 如果依赖多个用例，传入一个list即可
```@depend(['test_001', 'test_002'])```
  
### 发送邮件

```python
import testweb
from testweb.utils.mail import Mail


if __name__ == '__main__':
    testweb.main()
    mail = Mail(host='xx.com', user='xx@xx.com', password='xxx')
    mail.send_report(title='Demo项目测试报告', report_url='https://www.baidu.com', to_list=['xx@xx.com'])
```

- title：邮件标题
- report_url: 测试报告的url
- to_list: 接收报告的用户列表


### 发送钉钉

```python
import testweb
from testweb.utils.dingtalk import DingTalk


if __name__ == '__main__':
    testweb.main()
    dd = DingTalk(secret='xxx',
                  url='xxx')
    dd.send_report(msg_title='Demo测试消息', report_url='https://www.baidu.com')
```

- `secret`: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
- `url`: 钉钉机器人的Webhook链接
- `msg_title`: 消息标题
- `report_url`: 测试报告url

# Web UI 测试

## 下载浏览器和驱动

> kuto可以一键下载浏览器和驱动
通过`kuto`命令下载浏览和驱动，会自动下载chromium、webkit、firefox
```shell
> kuto --install
```

## 测试指定不同浏览器

在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`chrome`浏览器。


