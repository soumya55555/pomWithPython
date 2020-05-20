import unittest
import pytest
from selenium.webdriver import Chrome

class BaseTest():
    driver = Chrome(
        executable_path="C:\Installables_Selenium\chromedriver_win32 (2)\chromedriver.exe")
    def setupInitialization(self):

        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)






