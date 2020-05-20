from selenium import webdriver
from Test.BaseTest import BaseTest
class LoginPage(BaseTest):
    txt_userName_id="Email"
    txt_passWord_id="Password"
    btn_logIn_xpath="//input[@type='submit']"
    #Dashboard / nopCommerce administration
    text_to_verify_xpath="//h1[contains(text(),'Dashboard')]"
    link_logOut_xpath="//li/a[text()='Logout']"
    text_to_verify_afterLogout_xpath="//strong[text()='Welcome, please sign in!']"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.txt_userName_id).clear()
        self.driver.find_element_by_id(self.txt_userName_id).send_keys(username)
    def setPassWord(self,password):
        self.driver.find_element_by_id(self.txt_passWord_id).clear()
        self.driver.find_element_by_id(self.txt_passWord_id).send_keys(password)
    def clikOnLogin(self):
        self.driver.find_element_by_xpath(self.btn_logIn_xpath).click()
    def verifyText(self,text):
        self.assertEqual(self.driver.title(),text,"Text are not equal")
    def logout(self):
        self.driver.find_element_by_xpath(self.link_logOut_xpath).click()
        element=self.driver.find_element_by_xpath(self.text_to_verify_afterLogout_xpath)
        if element.is_displayed():
            print("Logout successful")
        else:
            print("Logout was unsuccessful")


