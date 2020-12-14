#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  unittest
from HTMLTestRunnerNew import HTMLTestRunner
from test_unittest_demo.common import path

from test_unittest_demo.testcase_ import caipiao_test_case
suite=unittest.TestSuite()
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(caipiao_test_case.caipiao_csae))
with open(path.path_1(),'wb' ) as f:
    test=HTMLTestRunner(
                        stream=f,
                       verbosity=4,                #详细程度
                       title='我的第一份测试报告',
                       description="第一份测试报告",
                       tester="啊志")
    test.run(suite)