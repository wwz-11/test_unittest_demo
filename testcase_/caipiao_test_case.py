#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  unittest
import  requests
from test_unittest_demo.common import excel_reading,log
from ddt import ddt,data,unpack
#读取数据
read_excel=excel_reading.Excel(r'D:\python\python代码\test_unittest_demo\data\caipiao.xlsx', 'Sheet1')  # 表格读取
test_data=read_excel.row_col_appointed_tuple([2,3,4,5,6,7],[1,2,3,4])
print(type(test_data))
print(test_data)
max_col=read_excel.max_column()

@ddt
class caipiao_csae(unittest.TestCase):
    def setUp(self):
        self.log=log.log().get_log()       #日志

    @data(*test_data)
    @unpack
    def test_1(self,row,url,data,rel):
        self.log.info("开始测试")
        a=requests.get(url,data)
        self.log.info("获得响应")
        expect=(a.json()["reason"])

        try:
            self.assertEqual(expect,rel)
            self.log.info("用例执行成功")
            result="通过"
            read_excel.write_data(int(row)+1,max_col,result)
        except Exception:
            self.log.error("用例执行失败")
            result = "未通过"
            read_excel.write_data(int(row)+1, max_col, result)


