import unittest
#from selenium.webdriver import Chrome
import HtmlTestRunner
import sys
sys.path.append("C://Users/spattanayak5/PycharmProjects/POMWithPython")
from Pages.LoginPage import LoginPage
from Test.BaseTest import BaseTest
from Pages.ProductsPage import ProductPage
import time
class ProductsTest(unittest.TestCase,BaseTest):
    global bt
    bt = BaseTest()

    @classmethod
    def setUpClass(cls):
        bt.setupInitialization()

    def test_login_click_on_products(self):
        lp = LoginPage(self.driver)
        lp.setUserName("admin@yourstore.com")
        lp.setPassWord("admin")
        lp.clikOnLogin()
        pp = ProductPage(self.driver)
        pp.clickonLinkCatalog()
        pp.clickonLinkProduct()
        pp.verifyTitle()
        pp.getAllTheProductsDetails()



    @classmethod
    def tearDownClass(cls):
        bt.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\spattanayak5\\PycharmProjects\\POMWithPython\\Reports"))
