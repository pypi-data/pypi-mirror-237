import os.path


case_content = """import testweb

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
"""

page_content = """from testweb import Page, Elem

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
"""

pub_content = """from page.web_page import IndexPage, LoginPage


class Pub(object):
    # 公共方法

    def __init__(self, driver):
        self.driver = driver
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def pwd_login(self, username="13652435335", password="wz123456@QZD"):
        # 账号密码登录流程
        self.index_page.loginBtn.click()
        self.login_page.pwdLoginTab.click()
        self.login_page.userInput.input(username)
        self.login_page.pwdInput.input(password)
        self.login_page.licenseBtn.click()
        self.login_page.loginBtn.click()
        self.login_page.firstCompanyIcon.click()
"""

run_content = """import testweb


if __name__ == '__main__':

    testweb.main(
        host='https://app-pre.qizhidao.com',
        case_path="tests"
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
    create_file(
        os.path.join(root_path, "tests", "test_web.py"),
        case_content,
    )
    create_file(
        os.path.join(root_path, "pages", "web_page.py"),
        page_content,
    )
    create_file(
        os.path.join(root_path, "pub.py"),
        pub_content,
    )
    create_file(
        os.path.join(root_path, "run.py"),
        run_content,
    )


