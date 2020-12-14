#!/usr/bin/python3
# _*_ coding:utf-8 _*_

from test_unittest_demo.pageLocators import login_locators

class Login():
    def __init__(self,driver):
        self.driver=driver
#登录
    def user_login(self,uname,passwod):
        self.driver.find_element_by_id(login_locators.Login_locator.user_login_name).send_keys(uname)
        self.driver.find_element_by_xpath(login_locators.Login_locator.user_login_paswod).send_keys(passwod)
        self.driver.find_element_by_css_selector(login_locators.Login_locator.user_login_login).click()
#忘记密码
    def forget_pwd(self):
        self.driver.find_element_by_xpath(*login_locators.Login_locator.forget_pwd_pwd).click()

# 获取弹框的内容
def get_alert_text(self):
    alert = self.driver.switch_to.alert
    return alert.text







