"""
@Author: kang.yang
@Date: 2023/5/16 14:37
"""
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


