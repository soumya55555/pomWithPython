import unittest
from selenium.webdriver import Chrome
import HtmlTestRunner
import sys
sys.path.append("C://Users/spattanayak5/PycharmProjects/POMWithPython")
from Pages.LoginPage import LoginPage
# from Pages import LoginPage
from Test.BaseTest import BaseTest

class LoginTest(unittest.TestCase,BaseTest):
    global bt
    bt=BaseTest()
    @classmethod
    def setUpClass(cls):
        bt.setupInitialization()
    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName("admin@yourstore.com")
        lp.setPassWord("admin")
        lp.clikOnLogin()
        lp.logout()


    @classmethod
    def tearDownClass(cls):
        bt.quit()






if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\spattanayak5\\PycharmProjects\\POMWithPython\\Reports"))