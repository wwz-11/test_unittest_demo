#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# @Time:2019/9/23 9:20
# @Email:1427245437@qq.com
import unittest
from day7 import Login
from day8 import Excel
from ddt import ddt,data,unpack
a=Excel.excel(r"D:\python\python代码\test_unittest_demo\data\2.xlsx","Sheet1")
shu_ju=a.reds_excel()
shu_ju.pop(0)
print(shu_ju)
new_shu_ju=[]
for i in shu_ju:
    l=[]
    l.append(i[2])
    l.append(str(i[3]))
    l.append(i[4])
    new_shu_ju.append(tuple(l))
print(new_shu_ju)
@ddt
class deng_lu_ddt_tset(unittest.TestCase):
    @data(*new_shu_ju)
    @unpack
    def test_login(self,uname,passwd,expect):
        print("test")
        rel=Login.login_check(uname,passwd)
        print('实际----', rel)
        print('预期----',expect)
        try:
            self.assertEqual(rel,expect)
            print('测试通过')
        except AssertionError:
            print('测试失败，预期与实际结果不用')
if __name__=="__main__":
    unittest.main()

