#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  unittest
import  requests
from test_unittest_demo.common import log,excel_reading
from ddt import ddt,data,unpack
#读取数据
read_excel=excel_reading.Excel(r'D:\python\python代码\test_unittest_demo\data\caipiao.xlsx', 'Sheet1')  # 表格读取
test_data=read_excel.row_col_appointed_tuple([2,3,4,5,6,7],[1,2])
print(test_data)
@ddt
class caipiao_csae(unittest.TestCase):
    def setUp(self):
        self.log=log.log().get_log()       #日志
    @data(test_data)
    @unpack
    def test_1(self,url,data):
        self.log.info("开始测试")
        a=requests.get(url,data)
        print(a.json()["reason"])








