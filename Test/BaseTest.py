import unittest
from selenium.webdriver import Chrome

class BaseTest():
    driver = Chrome(
        executable_path="C:\\Users\\spattanayak5\\PycharmProjects\\POMWithPython\\Drivers\\chromedriver.exe")
    def setupInitialization(self):
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def quit(self):
        self.driver.quit()




