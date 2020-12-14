#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# 2019/12/30/14:18
# @Email:1427245437@qq.com
import unittest
from time import sleep

from ddt import ddt,data, unpack
from selenium import webdriver
from test_unittest_demo.common import Excel, excel_reading
from test_unittest_demo.pageobjects import login_page, index_page

a=Excel.excel(r"D:\python\python代码\test_unittest_demo\data\chandao.xlsx","Sheet")
shu_ju=a.reds_excel()
shu_ju.pop(0)
# print(shu_ju)
new_shu_ju=[]
for i in shu_ju:
    l=[]
    l.append(int(i[1]))
    l.append(i[2])
    l.append(str(i[3]))
    new_shu_ju.append(tuple(l))

a=excel_reading.Excel(r"D:\python\python代码\test_unittest_demo\data\chandao.xlsx","Sheet")
shu_ju_succeed=a.row_appointed(2)
new_shu_ju_succeed=shu_ju_succeed[2:4:1]
print(new_shu_ju_succeed)
@ddt
class chan_dao_longin(unittest.TestCase):
    # 登录成功
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1/zentao/user-login")

    # def tearDown(self):
        # self.driver.quit()
    @data(new_shu_ju_succeed)
    @unpack
    def test_succeed(self,uname,passwod):
        sleep(2)
        #操作步骤
        login_page.Login(self.driver).user_login(uname,passwod)
        # 实际结果
        rel =index_page.Index(self.driver).isExist_login_ele()
        # 测试结果
        self.assertTrue(rel)

# if __name__ == "__main__":
#     unittest.main()