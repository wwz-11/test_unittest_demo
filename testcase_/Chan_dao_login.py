#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import unittest
from test_unittest_demo.common import excel_reading
from test_unittest_demo.common import Excel
from ddt import ddt,data,unpack
from selenium import webdriver
from test_unittest_demo.pageobjects import login_page,index_page

#表中读取数据
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
        self.driver.get("http://127.0.0.1/zentao/my/")

    def tearDown(self):
        self.driver.quit()
    @data(new_shu_ju_succeed)
    @unpack
    def test_succeed(self,uname,passwod):
        #操作步骤
        login_page.Login(self.driver).user_login(uname,passwod)
        # 实际结果
        rel =index_page.Index(self.driver).isExist_login_ele()
        # 测试结果
        try:
            self.assertTrue(rel)
            print("测试成功")
        except Exception:
            print("测试失败")

if __name__ == "__main__":
    unittest.main()