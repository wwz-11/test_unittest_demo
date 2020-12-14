#!/usr/bin/python3
# _*_ coding:utf-8 _*_
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Index():
    def __init__(self,driver):
        self.driver=driver
    #查看右上角 登录名是否存在
    #将右上角 登录名输入
    def isExist_login_ele(self):
        #如果存在就返回True，如果不存在，就返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='userNav']//span[1]")))
            return  True
        except :
            return False