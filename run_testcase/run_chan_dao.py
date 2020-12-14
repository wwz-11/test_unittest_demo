#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  unittest
from HTMLTestRunnerNew import HTMLTestRunner

from test_unittest_demo.testcase_ import Chan_dao
suite=unittest.TestSuite()
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(Chan_dao.chan_dao_test))
with open(r'D:\python\python代码\test_unittest_demo\output\report\4.html','wb' ) as f:
    test=HTMLTestRunner(
                        stream=f,
                       verbosity=4,                #详细程度
                       title='我的第一份测试报告',
                       description="第一份测试报告",
                       tester="啊志")
    test.run(suite)