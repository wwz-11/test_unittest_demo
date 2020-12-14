#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# @Time:2019/9/23 9:20
# @Email:1427245437@qq.com
import  unittest
from HTMLTestRunnerNew import HTMLTestRunner
from test_unittest_demo.common import path

from test_unittest_demo.testcase_ import zhu_ce
suite=unittest.TestSuite()
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(zhu_ce.zhu_ce_ddt_test))
with open(path.path_1(),'wb' ) as f:
    test=HTMLTestRunner(
                        stream=f,
                       verbosity=4,                #详细程度
                       title='我的第一份测试报告',
                       description="第一份测试报告",
                       tester="啊志")
    test.run(suite)